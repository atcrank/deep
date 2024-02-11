"""
simpleThought & associated Form hold content
simpleRelation is a tree of 'slots'
"""

import uuid

from django.contrib.auth.models import Group
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from treebeard import mp_tree


# Create your models here.
class SimpleThought(models.Model):
    """
    model: SimpleThought (id, content)
    - content is a Textfield.
    """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    content = models.TextField(default="")
    default_template = "prototype/content_simple_text.html"

    def url_for_post(self):
        return reverse(
            "prototype:location:simple_form",
            kwargs={"location": self.simplerelation_set.first().id, "content": self.id},
        )

    def id_for_html_element(self):
        return f"cont-{self.id}"


class SimpleRelation(mp_tree.MP_Node):
    """
    sr has one SimpleThought + one parent sr and 0-many children sr
    keeping it as simple as possible
    """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    content = models.ForeignKey(to=SimpleThought, on_delete=models.CASCADE, null=True)
    default_template = "prototype/tree.html"

    # add_child

    def url_for_get(self):
        return reverse("prototype:location:simple_form", kwargs={"location": self.id, "content": self.content.id})

    def url_for_debug(self):
        return reverse(
            "prototype:location:simple_tree",
            kwargs={"location": self.id, "content": self.content.id, "special_mode": "debug"},
        )

    def url_for_help(self):
        return reverse(
            "prototype:location:simple_tree",
            kwargs={"location": self.id, "content": self.content.id, "special_mode": "help"},
        )

    def url_for_hide(self):
        return reverse(
            "prototype:location:simple_tree",
            kwargs={"location": self.id, "content": self.content.id, "special_mode": "hide"},
        )

    def url_for_post(self):
        # reserved for jqui updates: e.g.  drag actions, sort actions etc
        pass

    def url_for_put(self):
        return reverse(
            "prototype:location:simple_form_add_sibling", kwargs={"location": self.id, "content": self.content.id}
        )

    # add sibling
    def url_for_patch(self):
        return reverse(
            "prototype:location:simple_form_add_child", kwargs={"location": self.id, "content": self.content.id}
        )

    def url_for_delete(self):
        return reverse("prototype:location:simple_form", kwargs={"location": self.id, "content": self.content.id})

    def id_for_html_element(self):
        return f"cont-loc-{ self.id }"


class Structure(mp_tree.MP_Node):
    """Project, Page and subsection structure model
    - root = project
    - 1st level = page (optional)
    - lower levels = sections"""

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField(null=True)  # meaning all db rows of type, use for admin(?)
    content_object = GenericForeignKey("content_type", "object_id")
    target_groups = models.ManyToManyField(Group)

    def url_for_get(self):
        return reverse("prototype:location:simple_form", kwargs={"location": self.id, "content": self.content.id})

    def url_for_post(self):
        # reserved for jqui updates: e.g.  drag actions, sort actions etc
        pass

    def url_for_put(self):
        return reverse(
            "prototype:location:simple_form_add_child", kwargs={"location": self.id, "content": self.content.id}
        )

    # add sibling
    def url_for_patch(self):
        return reverse(
            "prototype:location:simple_form_add_sibling", kwargs={"location": self.id, "content": self.content.id}
        )

    def url_for_delete(self):
        return reverse("prototype:location:simple_form", kwargs={"location": self.id, "content": self.content.id})
