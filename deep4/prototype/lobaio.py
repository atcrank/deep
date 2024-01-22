"""
locality of behavior, all in one

A single file that holds the model, form, view and template settings

"""
import uuid
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django import forms
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from django.forms.widgets import Textarea
from .models import SimpleRelation, SimpleThought, OrderedRelationShip
from treebeard import mp_tree

def get_all_nodes(request):
    context = {'location_list': SimpleRelation.get_root_nodes()}
    return render(request, 'prototype/root.html', context)
class SimpleThoughtForm(forms.ModelForm):
    template_name = 'prototype/forms/SimpleThoughtForm.html'
    class Meta:
        model = SimpleThought
        fields = ['content',]
        widgets = {'content': Textarea(attrs={"cols": 70, "rows": 2})}

class OrderedThoughtForm(forms.ModelForm):
    template_name = 'prototype/forms/OrderedThoughtForm.html'
    class Meta:
        model=OrderedRelationShip
        fields=['number',]

def get_tree(request, location):
    context = {'location' : SimpleRelation.objects.get(id=location)}
    if request.htmx:
        template_name = 'prototype/tree.html'
    else:
        template_name = 'prototype/root.html'
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

    def get(self, request, location, content=None):
        """gets a form that holds the editable content"""
        print("HTMX", dir(request.htmx), request.htmx.trigger_name)
        sr_instance = self.relation_model.objects.get(id=location)
        stf = self.model_form_class(instance=sr_instance.content)
        return render(request, SimpleThoughtForm.template_name, {'form': stf, 'location': location})

    def patch(self, request, location, content=None):
        """"add child location to location, provide empty form."""
        sr_instance = self.relation_model.objects.get(id=location)
        st_instance = self.model_class.objects.create(content="new entry")
        sr_instance.add_child(content=st_instance)
        return get_tree(request, sr_instance.id, st_instance.id)

    def put(self, request, location, content=None):
        """add a sibling node at this depth"""
        sr_instance = self.relation_model.objects.get(id=location)
        st_instance = self.model_class.objects.create(content="new entry")
        if sr_instance.is_root():
            new_sr = self.relation_model.add_root(content=st_instance)
        else:
            new_sr = sr_instance.get_parent().add_child(content=st_instance)
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


