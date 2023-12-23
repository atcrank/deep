from django.urls import path
from .lobaio import get_simplethoughttree, get_all_nodes

app_name = "prototype"
urlpatterns = [
    path("", get_all_nodes, name='get_all_nodes'),
    path("<uuid:id>/", get_simplethoughttree, name="simple_tree"),
               ]
