from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to our University.")


def detail(request, pk):
    return HttpResponse(f"Details of department with id {pk}")


def update(request, pk):
    return HttpResponse(f"You're department faculty with id {pk}")
