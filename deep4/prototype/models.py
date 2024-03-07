"""
Models are: Location (Treebeard MP_Node) - instances point to:
Content Objects through generic foreign keys
Illustrative Content Object Models:
- Plaintext
- RichText

Lightweight HTML sanitisation from Adam Johnson using nh3
- https://adamj.eu/tech/2023/12/13/django-sanitize-incoming-html-nh3/

- To adjust the allowed tags:
tags = nh3.ALLOWED_TAGS - {"b"}

- To amend allowed attributes:
from copy import deepcopy
attributes = deepcopy(nh3.ALLOWED_ATTRIBUTES)
attributes["img"].add("data-invert")
nh3.clean("<img src='example.jpeg' data-invert=true>", attributes=attributes)

TODO: Is it a security problem to allow font attributes or styles?
"""

import uuid
from copy import deepcopy

import nh3
from django import forms
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from treebeard import mp_tree


class HtmlSanitizedCharField(forms.CharField):
    allowed_tags = deepcopy(nh3.ALLOWED_TAGS)
    allowed_tags.add("font")
    allowed_attributes = deepcopy(nh3.ALLOWED_ATTRIBUTES)
    allowed_attributes.update({"font": {"size", "color", "style"}})
    print(f"{allowed_attributes=}")

    def to_python(self, value):
        value = super().to_python(value)
        if value not in self.empty_values:
            value = nh3.clean(value, tags=self.allowed_tags, attributes=self.allowed_attributes)
        return value


class HtmlSanitizedTextField(models.TextField):
    def formfield(self, form_class=HtmlSanitizedCharField, **kwargs):
        return super().formfield(form_class=form_class, **kwargs)


class PlainText(models.Model):
    """
    model: PlainText (id, content)
    - content is a Textfield.
    """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    content = models.TextField(default="")
    default_template = "prototype/plaintext/content_display.html"
    name = "PlainText"

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
    model: RichText (id, content)
    - content is a simplified, sanitized HTML.
    """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    content = HtmlSanitizedTextField(default="<h1>new rich entry</h1>")
    default_template = "prototype/richtext/content_display.html"
    name = "RichText"

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
    content_object = GenericForeignKey("content_type", "object_id")
    default_template = "prototype/tree_ol.html"
    name = "Location"

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
        return reverse("prototype:location:add_sibling", kwargs={"location": self.id})

    # add sibling
    def url_for_patch(self):
        return reverse("prototype:location:add_child", kwargs={"location": self.id})

    def url_for_delete(self):
        return reverse("prototype:location:delete", kwargs={"location": self.id})

    def id_for_html_element(self):
        return f"cont-loc-{ self.id }"
