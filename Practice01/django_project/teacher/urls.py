from django.urls import path

from .views import teacher_home_page_view, teacher_report_page_view

urlpatterns = [
    path("", teacher_home_page_view, name="teacher home"),
    path("report/", teacher_report_page_view, name="teacher report"),
]
