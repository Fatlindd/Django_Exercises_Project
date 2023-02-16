from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to our University.")


def detail(request, pk):
    return HttpResponse(f"Details of department with id {pk}")

