from django.http import HttpResponse
from .models import Course


def home(request):
    courses = Course.objects.all()
    output = ''.join([f'<p>{course.name}</p>' for course in courses])
    return HttpResponse(output)


def detail(request, pk):
    course = Course.objects.get(pk=pk)
    students = course.student_set.all()
    students = ''.join([f'{student.first_name} {student.last_name} ' for student in students])
    output = f'<i>Name: </i> <b>{course.name}</b><br><i>Students:</i> <b>{students}</b>'
    return HttpResponse(output)
