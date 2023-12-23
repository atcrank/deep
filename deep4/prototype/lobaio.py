"""
locality of behavior, all in one

A single file that holds the model, form, view and template settings

"""
import uuid
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.forms import ModelForm
from django.shortcuts import render
from django.forms.widgets import Textarea
from .models import SimpleRelation, SimpleThought
from treebeard import mp_tree

# class SimpleThought(models.Model):
#     id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
#     content = models.TextField()
#
# class SimpleRelation(mp_tree):
#     """
#     sr has one SimpleThought + one parent sr and 0-many children sr
#     keeping it as simple as possible
#     """
#     id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
#     content = models.ForeignKey(to=SimpleThought, on_delete=models.CASCADE, null=True)

class SimpleThoughtForm(ModelForm):
    template_name = 'prototype/forms/SimpleThoughtForm.html'
    class Meta:
        model = SimpleThought
        fields = ['content',]
        widgets = {'content': Textarea(attrs={"cols": 80, "rows": 20})}

def get_simplethoughttree(request, id):
    context = {'node' : SimpleRelation.objects.get(id=id)}
    if request.htmx:
        template_name = 'prototype/forms/SimpleThoughtForm.html'
    else:
        template_name = 'prototype/root.html'
    return render(request, template_name, context)

def get_all_nodes(request):
    context = {'node_list': SimpleRelation.objects.all()}
    return render(request, 'prototype/node_list.html', context)

