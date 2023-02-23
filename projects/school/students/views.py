from django.http import HttpResponse
from .models import Student


def home(request):
    students = Student.objects.all()
    output = '<br>'.join([f'{student.full_name()}' for student in students])
    return HttpResponse(output)

