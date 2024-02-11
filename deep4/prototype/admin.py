from django.contrib import admin

# Register your models here.
from .models import SimpleRelation, SimpleThought, Structure

admin.site.register(SimpleThought)
admin.site.register(SimpleRelation)
admin.site.register(Structure)
