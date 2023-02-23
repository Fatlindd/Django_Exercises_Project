from django.http import HttpResponse
from .models import Department


def home(request):
    departments = Department.objects.all()
    output = ''.join([f'<h2>{departments}</h2>' for department in departments])
    return HttpResponse(output)


def detail(request, pk):
    department = Department.objects.get(pk=pk)
    students = department.student_set.all()
    students = [f'{student.first_name} {student.last_name}' for student in students]
    students = ', '.join(students)
    s = f'Name: <i>{}</i><br>Opened on: <i>{}</i><br>Students: <i>{}</i>'
    return HttpResponse(s.format(department.name, department.opened_on, students))


def update(request, pk):
    return HttpResponse(f"You're department faculty with id {pk}")


def delete(request, pk):
    return HttpResponse(f"You're deleting department with id pk {pk}")
