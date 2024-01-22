from django.urls import path
from .lobaio import get_tree, get_all_nodes, SimpleThoughtFormView

app_name = "prototype"
urlpatterns = [
    path("", get_all_nodes, name='get_all_nodes'),
    path("<uuid:location>/", get_tree, name="blank_location"),
    path("<uuid:location>/<uuid:content>/", get_tree, name="simple_tree"),
    path("<uuid:location>/<uuid:content>/form", SimpleThoughtFormView.as_view(), name="simple_form"),
    path("<uuid:location>/<uuid:content>/add_child", SimpleThoughtFormView.as_view(), name="simple_form_add_child"),
    path("<uuid:location>/<uuid:content>/add_sibling", SimpleThoughtFormView.as_view(), name="simple_form_add_sibling"),
               ]
