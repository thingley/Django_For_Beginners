from django.http import HttpResponse


def teacher_home_page_view(request):
    return HttpResponse("Hello Teacher!")


def teacher_report_page_view(request):
    return HttpResponse("Teacher Report Page!")
