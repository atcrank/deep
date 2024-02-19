"""
simpleThought & associated Form hold content
simpleRelation is a tree of 'slots'
"""

import uuid

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from treebeard import mp_tree


# Create your models here.
class PlainText(models.Model):
    """
    model: PlainText (id, content)
    - content is a Textfield.
    """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    content = models.TextField(default="")
    default_template = "prototype/plaintext/content_display.html"

    def url_for_get(self):
        return reverse(
            "prototype:content:content_form",
            kwargs={"content_type": "plaintext", "content": self.id},
        )

    def url_for_post(self):
        return reverse(
            "prototype:content:content_form",
            kwargs={"content_type": "plaintext", "content": self.id},
        )

    def id_for_html_element(self):
        return f"cont-{self.id}"


class RichText(models.Model):
    """
    model: SimpleThought (id, content)
    - content is a Textfield.
    """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    content = models.TextField(default="<h1>new rich entry</h1>")
    default_template = "prototype/richtext/content_display.html"

    def url_for_get(self):
        return reverse(
            "prototype:content:content_form",
            kwargs={"content_type": "richtext", "content": self.id},
        )

    def url_for_post(self):
        return reverse(
            "prototype:content:content_form",
            kwargs={"content_type": "richtext", "content": self.id},
        )

    def id_for_html_element(self):
        return f"cont-{self.id}"


class Location(mp_tree.MP_Node):
    """
    sr has one SimpleThought + one parent sr and 0-many children sr
    keeping it as simple as possible
    """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    content_type = models.ForeignKey(to=ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.UUIDField()
    default_template = "prototype/tree.html"
    content_object = GenericForeignKey("content_type", "object_id")

    # add_child
    def url_for_add_root(self):
        return reverse("prototype:location")

    def url_for_get(self):
        return reverse("prototype:content_form", kwargs={"content_object": self.content_object.id})

    def url_for_debug(self):
        return reverse(
            "prototype:location:mode_tree",
            kwargs={"location": self.id, "special_mode": "debug"},
        )

    def url_for_help(self):
        return reverse(
            "prototype:location:mode_tree",
            kwargs={"location": self.id, "special_mode": "help"},
        )

    def url_for_hide(self):
        return reverse(
            "prototype:location:mode_tree",
            kwargs={"location": self.id, "special_mode": "hide"},
        )

    def url_for_post(self):
        # reserved for jqui updates: e.g.  drag, sort, resize actions etc
        pass

    def url_for_put(self):
        return reverse("prototype:location:form_add_sibling", kwargs={"location": self.id})

    # add sibling
    def url_for_patch(self):
        return reverse("prototype:location:form_add_child", kwargs={"location": self.id})

    def url_for_delete(self):
        return reverse("prototype:location:content_form", kwargs={"location": self.id})

    def id_for_html_element(self):
        return f"cont-loc-{ self.id }"
