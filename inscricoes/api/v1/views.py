from django.http import HttpResponse


def index(request):
    return HttpResponse(content="", status=200)
