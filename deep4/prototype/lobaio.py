"""
locality of behavior, all in one

A single file that holds the forms and views.

Can we get models and templates in here too?
"""

from django import forms
from django.forms.widgets import Textarea
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import SimpleRelation, SimpleThought


def get_all_nodes(request, special_mode=None):
    context = {"location_list": SimpleRelation.get_root_nodes()}
    template_sub_dir = ""
    if special_mode:
        context.update({"special_mode": special_mode})
    if special_mode == "row_col":
        template_sub_dir = "row_col/"
    return render(request, f"prototype/{template_sub_dir}root.html", context)


class SimpleThoughtForm(forms.ModelForm):
    template_name = "prototype/forms/SimpleThoughtForm.html"

    class Meta:
        model = SimpleThought
        fields = [
            "content",
        ]
        widgets = {"content": Textarea(attrs={"cols": 70, "rows": 1, "autofocus": True})}


def get_tree(request, location, content=None, special_mode=None):
    context = {"location": SimpleRelation.objects.get(id=location)}
    template_sub_dir = ""
    if special_mode == "help":
        context.update({"help": context["location"].content.__class__.__doc__})
    elif special_mode == "debug":
        context.update({"id": context["location"].content_id})
    elif special_mode == "hide":
        pass
    elif special_mode == "row_col":
        template_sub_dir = "row_col/"
    if request.htmx:
        template_name = f"prototype/{template_sub_dir}tree.html"
    else:
        context.update({"location_list": [context["location"]]})
        template_name = f"prototype/{template_sub_dir}root.html"
    print("Template_Name", template_name)
    return render(request, template_name, context)


class SimpleThoughtFormView(View):
    """The FormView for the SimpleThoughtForm:
    provides actions for
    get - returns an editable form
    post - updates the value
    button actions for
          add child, add sibling and delete nodes."""

    model_class = SimpleThought
    model_form_class = SimpleThoughtForm
    relation_model = SimpleRelation

    def get(self, request, location, content):
        """gets a form that holds the editable content"""
        print(request, location, content)
        sr_instance = self.relation_model.objects.get(id=location)
        match content:
            case "help":
                return get_tree(request, sr_instance.id, {"help": location.content.__class__.__doc__})
            case _:
                stf = self.model_form_class(instance=sr_instance.content)
        return render(request, SimpleThoughtForm.template_name, {"form": stf, "location": location})

    def patch(self, request, location, content=None):
        """ "add child location to location, provide empty form."""
        sr_instance = self.relation_model.objects.get(id=location)
        st_instance = self.model_class.objects.create(content="new entry")
        sr_instance.add_child(content=st_instance)
        return get_tree(request, sr_instance.id, st_instance.id)

    def put(self, request, location=None, content=None):
        """add a sibling node at this depth"""
        st_instance = self.model_class.objects.create(content="new entry")
        if location:
            sr_instance = self.relation_model.objects.get(id=location)
            if sr_instance.is_root():
                new_sr = self.relation_model.add_root(content=st_instance)
            else:
                new_sr = sr_instance.get_parent().add_child(content=st_instance)
        else:
            new_sr = self.relation_model.add_root(content=st_instance)

        return get_tree(request, new_sr.id, st_instance.id)

    def post(self, request, location, content=None):
        """update the content of the node."""
        st_instance = self.model_class.objects.get(id=content)
        stf = self.model_form_class(request.POST, instance=st_instance)
        if stf.is_valid():
            stf.save()
            return get_tree(request, location, content)
        else:
            print(stf)

    def delete(self, request, location, content):
        """delete this node and the nodes below it."""
        st_instance = self.model_class.objects.get(id=content)
        sr_instance = self.relation_model.objects.get(id=location)
        if st_instance.simplerelation_set.count() == 1:
            st_instance.delete()
        sr_instance.delete()
        return HttpResponse("")
