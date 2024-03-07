from django.urls import include, path

from deep4.prototype.lobaio import ContentModelFormView, LocationView, get_trees, page_view, project_view

app_name = "prototype"

content_urls = [
    # path("", get_tree, name="single_tree"),
    # path("add_child", ContentModelFormView.as_view(), name="form_add_child"),  # put
    # path("add_sibling", ContentModelFormView.as_view(), name="form_add_sibling"),  # patch
    path("form", ContentModelFormView.as_view(), name="content_form"),  # delete
    # path("<str:special_mode>", get_tree, name="mode_tree"),  # help, debug
]

location_urls = [
    path("tree", LocationView.as_view(), name="get_tree"),  # get
    path("add_child", LocationView.as_view(), name="add_child"),  # put
    path("add_sibling", LocationView.as_view(), name="add_sibling"),  # patch
    path("delete", LocationView.as_view(), name="delete"),  # delete
    path("<str:special_mode>", LocationView.as_view(), name="mode_tree"),  # help, debug
    path("<uuid:target_loc>/<str:loc_name>", LocationView.as_view(), name="move"),  # post
]

# content_forms = [
#     path("form", ContentModelFormView.as_view(), name="content_form"),  # post
# ]

urlpatterns = [
    path("location/<uuid:location>/", include((location_urls, "location"))),
    # path("location2/<uuid:location>/", include((location_urls, "location2"))),
    path("<str:content_type>/<uuid:content>/", include((content_urls, "content"))),
    path("<str:content_type>/add_root/", ContentModelFormView.as_view(), name="add_root_type"),
    path("add_root/", ContentModelFormView.as_view(), name="add_root"),
    path("", get_trees, name="home"),
    path("project/<uuid:location>/<int:page_no>/", page_view, name="page"),
    path("project/<uuid:location>/", project_view, name="project"),
]
