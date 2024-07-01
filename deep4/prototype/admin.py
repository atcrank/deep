from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

# Register your models here.
from .models import Frame, Location, PlainText, RichText


@admin.register(Location)
class LocationAdmin(TreeAdmin):
    form = movenodeform_factory(Location)
    fields = ("id", "content_type", "object_id", "content_object", "frame")
    list_display = ("id", "content_type", "object_id", "content_object", "frame")
    list_editable = ("frame",)


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    fields = ("name", "child_group_tag", "child_element_tag")


admin.site.register(PlainText)
admin.site.register(RichText)
