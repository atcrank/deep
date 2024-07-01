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

TODO: Is it a security problem to allow e.g. font attributes or styles?
"""

import uuid
from copy import deepcopy

import nh3
from django import forms
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from treebeard import mp_tree


class HtmlSanitizedCharField(forms.CharField):
    allowed_tags = deepcopy(nh3.ALLOWED_TAGS)
    allowed_tags.add("font")
    allowed_attributes = deepcopy(nh3.ALLOWED_ATTRIBUTES)
    allowed_attributes.update({"font": {"size", "color", "style"}})

    def to_python(self, value):
        value = super().to_python(value)
        if value not in self.empty_values:
            value = nh3.clean(
                value, tags=self.allowed_tags, attributes=self.allowed_attributes
            )
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


LI = "li"
UL = "ul"
DIVROW = "div class='row border'"
DIVCOL = "div class='col-sm border'"
SVG = "svg"
H1 = "h1"
H3 = "h3"
H5 = "h5"

NODE_TAG_CHOICES = (
    (LI, "list item"),
    (DIVROW, "row"),
    (DIVCOL, "column"),  # good for Node
    (H1, "1 - heading"),
    (H3, "3 - heading"),
    (H5, "5 - heading"),
)

CHILDREN_TAG_CHOICES = (
    (UL, "list"),
    (DIVROW, "row"),
    (DIVCOL, "column"),
)  # good for children


class Frame(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.TextField()
    short_description = models.TextField()
    child_group_tag = models.TextField(default="ul", choices=CHILDREN_TAG_CHOICES)
    child_element_tag = models.TextField(default="li", choices=NODE_TAG_CHOICES)

    def __str__(self):
        return self.name

    def child_element_tag_open(self):
        return mark_safe(f"<{self.child_element_tag}")

    def child_element_tag_close(self):
        return mark_safe(f"</{self.child_element_tag}>")

    def children_tag_open(self):
        return mark_safe(f"<{self.child_group_tag}")

    def children_tag_close(self):
        return mark_safe(f"</{self.child_group_tag}>")


class Location(mp_tree.MP_Node):
    """
    Location objects anchor content objects in a tree and wrap it in a variable node_tag and a
    """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    content_type = models.ForeignKey(
        to=ContentType, on_delete=models.CASCADE, null=True
    )
    object_id = models.UUIDField()
    content_object = GenericForeignKey("content_type", "object_id")
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE, null=True, blank=True)
    default_template = "prototype/tree.html"
    name = "Location"

    # add_child
    def url_for_add_root(self):
        return reverse("prototype:location")

    def url_for_get(self):
        return reverse(
            "prototype:content_form", kwargs={"content_object": self.content_object.id}
        )

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
        # consider use of format_html here
        return f"loc-{ self.id }"
