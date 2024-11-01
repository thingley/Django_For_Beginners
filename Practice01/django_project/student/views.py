from django.views.generic import TemplateView


# StudentHomePageView inherits from TemplateView
class StudentHomePageView(TemplateView):
    template_name = "student_home.html"


# StudentAboutPageView inherits from TemplateView
class StudentAboutPageView(TemplateView):
    template_name = "student_about.html"


# StudentAboutPageView inherits from TemplateView
class StudentTestPageView(TemplateView):
    template_name = "student_test.html"
