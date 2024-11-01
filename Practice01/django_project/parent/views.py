from django.http import HttpResponse


def parent_home_page_view(request):
    return HttpResponse("Hello Parent!")


def parent_info_page_view(request):
    return HttpResponse("Parent Info Page!")
