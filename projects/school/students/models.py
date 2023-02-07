from django.db import models
from courses.models import Course


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
