from django.http import HttpResponse
from .models import Student


def home(request):
    students = Student.objects.all()
    output = ''.join([f'{student.first_name} {student.last_name}<br>' for student in students])
    return HttpResponse(output)


def detail(request, pk):
    return HttpResponse(f"Details of student with id {pk}")


def update(request, pk):
    return HttpResponse(f"You're updating student with id {pk}.")


def delete(request, pk):
    return HttpResponse(f"You're deleting student with id {pk}.")
