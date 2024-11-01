from django.urls import path

from .views import parent_home_page_view, parent_info_page_view

urlpatterns = [
    path("", parent_home_page_view, name="parent home"),
    path("info/", parent_info_page_view, name="parent info"),
]
