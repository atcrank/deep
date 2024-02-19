from django.contrib import admin

# Register your models here.
from .models import Location, PlainText, RichText

admin.site.register(PlainText)
admin.site.register(RichText)
admin.site.register(Location)
