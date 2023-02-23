from django.http import HttpResponse
from .models import Department


def home(request):
    departments = Department.objects.all()
    output = ''.join([f'<h2>{departments}</h2>' for department in departments])
    return HttpResponse(output)


def detail(request, pk):
    return HttpResponse(f"Details of department with id {pk}")


def update(request, pk):
    return HttpResponse(f"You're department faculty with id {pk}")


def delete(request, pk):
    return HttpResponse(f"You're deleting department with id pk {pk}")
