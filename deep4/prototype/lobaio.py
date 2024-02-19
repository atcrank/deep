"""
locality of behavior, all in one

A single file that holds the forms and views.

Can we get models and templates in here too?
"""

from django import forms
from django.contrib.contenttypes.models import ContentType
from django.forms.widgets import Textarea
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Location, PlainText, RichText


def get_trees(request, special_mode=None):
    model_class = Location
    context = {"location_list": model_class.get_root_nodes()}
    template_sub_dir = ""
    return render(request, f"prototype/{template_sub_dir}root.html", context)


def get_tree(request, location, special_mode=None):
    model_class = Location
    loc = model_class.objects.get(id=location)
    context = {"location": loc, "content_object": loc.content_object}
    template_sub_dir = ""
    if special_mode == "help":
        context.update({"help": context["location"].content_object.__class__.__doc__})
    elif special_mode == "debug":
        context.update({"db": f"loc={context['location'].id}; content= {context['location'].content_object.id}"})
    elif special_mode == "hide":
        print("hide button")

    if request.htmx and not request.POST:
        template_name = "prototype/tree.html"
    elif request.POST:
        template_name = f"prototype/{location.content_type.model}content_display.html"
    else:
        context.update({"location_list": [context["location"]]})
        template_name = f"prototype/{template_sub_dir}tree.html"

    print(f"{context=}-{template_name=}")
    return render(request, template_name, context)


class PlainTextForm(forms.ModelForm):
    template_name = "prototype/plaintext/PlainTextForm.html"

    class Meta:
        model = PlainText
        fields = [
            "content",
        ]
        widgets = {"content": Textarea(attrs={"cols": 70, "rows": 1, "autofocus": True})}


class RichTextForm(forms.ModelForm):
    template_name = "prototype/richtext/RichTextForm.html"

    class Meta:
        model = RichText
        fields = [
            "content",
        ]
        widgets = {"content": Textarea(attrs={"hidden": True})}


FORMS = {"location": None, "plaintext": PlainTextForm, "richtext": RichTextForm}


class ContentModelFormView(View):
    """The FormView for the SimpleTextForm:
    provides actions for
    get - returns an editable form
    post - updates the value
    button actions for
          add child, add sibling and delete nodes."""

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        if kwargs.get("location"):
            self.location_model_class = Location
            self.location = self.location_model_class.objects.get(id=kwargs.get("location"))
            self.content = self.location.content_object
            self.model_class = self.content.__class__
            self.model_form_class = FORMS[self.location.content_type.model]
            self.template = self.content.default_template
            # self.context = add_to_context(self.context, [self.location, self.content])
        elif kwargs.get("content_type"):
            self.model_class = ContentType.objects.get(
                app_label="prototype", model=kwargs.get("content_type")
            ).model_class()
            if kwargs.get("content"):
                self.content = self.model_class.objects.get(id=kwargs.get("content"))
            self.template = self.model_class.default_template
            self.model_form_class = FORMS[kwargs.get("content_type")]
            self.location_model_class = Location
        else:
            self.location_model_class = Location

    def get(self, request, content_type, content, special_mode=None):
        """gets a form that holds the editable content"""
        match special_mode:
            case "help":
                return get_tree(request, self.location.id, "help")
            case "debug":
                return get_tree(request, self.location.id, "db")
            case _:
                stf = self.model_form_class(instance=self.content)
        return render(request, self.model_form_class.template_name, {"form": stf})

    def patch(self, request, location, special_mode=None):
        """ "add child location to location, provide default content."""
        pt_instance = self.model_class.objects.create(content="new entry")
        self.location.add_child(content_object=pt_instance)
        return get_tree(request, self.location.id)

    def put(self, request, location=None, content_type="plaintext", special_mode=None):
        """add a sibling node at this depth"""
        content_instance = self.model_class.objects.create(content="new entry")
        if location:
            loc_instance = self.location_model_class.objects.get(id=location)
            if loc_instance.is_root():
                new_loc = self.location_model_class.add_root(content_object=content_instance)
            else:
                new_loc = loc_instance.get_parent().add_child(content_object=content_instance)
        else:
            new_loc = self.location_model_class.add_root(content_object=content_instance)

        return get_tree(request, new_loc.id)

    def post(self, request, content_type, content, special_mode=None):
        """update the content of the node."""
        print(request.POST)
        content_form = self.model_form_class(request.POST, instance=self.content)
        if content_form.is_valid():
            content_object = content_form.save()
            return render(
                request,
                template_name=f"prototype/{content_type}/content_display.html",
                context={"content_object": content_object},
            )
        else:
            print(content_form.errors)

    def delete(self, request, location):
        """delete this node and the nodes below it."""
        # I believe this deletes sub-locations but maybe not content  ??
        self.location.delete()
        return HttpResponse("")


def add_to_context(context, *variables):
    for v in variables:
        context.update({f"{v=}".split("=")[0]: v})
    return context
