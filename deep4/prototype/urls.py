from django.urls import include, path

from deep4.prototype.lobaio import ContentModelFormView, get_tree, get_trees

app_name = "prototype"

content_urls = [
    path("", get_tree, name="single_tree"),
    path("add_child", ContentModelFormView.as_view(), name="form_add_child"),  # put
    path("add_sibling", ContentModelFormView.as_view(), name="form_add_sibling"),  # patch
    path("form", ContentModelFormView.as_view(), name="content_form"),  # delete
    path("<str:special_mode>", get_tree, name="mode_tree"),  # help, debug
]

content_forms = [
    path("form", ContentModelFormView.as_view(), name="content_form"),  # post
]

urlpatterns = [
    path("location/<uuid:location>/", include((content_urls, "location"))),
    path("<str:content_type>/<uuid:content>/", include((content_forms, "content"))),
    path("<str:content_type>/add_root/", ContentModelFormView.as_view(), name="add_root_type"),
    path("add_root/", ContentModelFormView.as_view(), name="add_root"),
    path("", get_trees, name="get_trees"),
]
