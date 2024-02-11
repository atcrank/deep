from django.urls import include, path

from .lobaio import SimpleThoughtFormView, get_proj, get_thought_nodes, get_thought_tree

app_name = "prototype"

content_urls = [
    path("", get_thought_tree, name="single_tree"),
    path("<uuid:content>/form", SimpleThoughtFormView.as_view(), name="simple_form"),  # post, delete
    path("<uuid:content>/add_child", SimpleThoughtFormView.as_view(), name="simple_form_add_child"),  # put
    path("<uuid:content>/add_sibling", SimpleThoughtFormView.as_view(), name="simple_form_add_sibling"),  # patch
    path("<uuid:content>/<str:special_mode>", get_thought_tree, name="simple_tree"),  # help, debug
]

location_urls = [
    path("<uuid:location>/", include((content_urls, "location"))),
    path("add_root/", SimpleThoughtFormView.as_view(), name="simple_form_add_root"),
    path("", get_thought_nodes, name="get_thought_nodes"),
]

urlpatterns = [
    path("proj/<uuid:proj_id>/page/<int:page_at>/depth/<int:depth>/<page_no>/", get_proj, name="proj"),
    path("", include(location_urls)),
]
