from django.http import HttpResponse


def home(request):
    return HttpResponse("Students.")


def detail(request, pk):
    return HttpResponse(f"Details of student with id {pk}")


def update(request, pk):
    return HttpResponse(f"You're updating student with id {pk}.")


def delete(request, pk):
    return HttpResponse(f"You're deleting student with id {pk}.")
