from django.urls import include, path

from .lobaio import SimpleThoughtFormView, get_all_nodes, get_tree

app_name = "prototype"

content_urls = [
    path("", get_tree, name="single_tree"),
    path("<uuid:content>/form", SimpleThoughtFormView.as_view(), name="simple_form"),
    path("<uuid:content>/add_child", SimpleThoughtFormView.as_view(), name="simple_form_add_child"),
    path("<uuid:content>/add_sibling", SimpleThoughtFormView.as_view(), name="simple_form_add_sibling"),
    path("<uuid:content>/<str:special_mode>", get_tree, name="simple_tree"),
]

location_urls = [
    path("<uuid:location>/", include((content_urls, "location"))),
    path("add_root/", SimpleThoughtFormView.as_view(), name="simple_form_add_root"),
    path("", get_all_nodes, name="get_all_nodes"),
]

urlpatterns = [path("", include(location_urls))]
