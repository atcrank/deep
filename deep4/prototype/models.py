"""
simpleThought & associated Form hold content
simpleRelation is a tree of 'slots'
"""

import uuid

from django.db import models
from treebeard import mp_tree


# Create your models here.
class SimpleThought(models.Model):
    """
    model: SimpleThought (id, content)
    - content is a Textfield.
    """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    content = models.TextField(default="")


class SimpleRelation(mp_tree.MP_Node):
    """
    sr has one SimpleThought + one parent sr and 0-many children sr
    keeping it as simple as possible
    """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    content = models.ForeignKey(to=SimpleThought, on_delete=models.CASCADE, null=True)
