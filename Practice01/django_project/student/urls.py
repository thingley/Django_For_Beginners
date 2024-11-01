from django.urls import path
from .views import StudentHomePageView, StudentAboutPageView, StudentTestPageView

urlpatterns = [
    path("", StudentHomePageView.as_view(), name="student home"),
    path("about/", StudentAboutPageView.as_view(), name="student about"),
    path("test/", StudentTestPageView.as_view(), name="student test"),
]
