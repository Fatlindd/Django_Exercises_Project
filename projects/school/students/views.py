from django.http import HttpResponse
from .models import Student


def home(request):
    students = Student.objects.all()
    output = '<br>'.join([f'{student.full_name()}' for student in students])
    return HttpResponse(output)


def detail(request, pk):
    student = Student.objects.get(pk=pk)
    s = '<i>Name:</i> {}<br><i>Age:</i>{}<br><i>Course: {}</i>'
    return HttpResponse(s.format(student.full_name(), student.age, student.course))
