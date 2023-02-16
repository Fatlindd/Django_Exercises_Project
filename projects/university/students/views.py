from django.http import HttpResponse


def home(request):
    return HttpResponse("Students.")


def detail(request, pk):
    return HttpResponse(f"Details of student with id {pk}")
