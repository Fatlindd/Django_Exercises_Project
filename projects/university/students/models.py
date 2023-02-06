from django.db import models

from projects.university.departments.models import Department


class Student(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

