from django.db import models
from core.models import TimeStampedModel


class Student(TimeStampedModel):

    student_code = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    guardian_name = models.CharField(max_length=100)
    guardian_phone = models.CharField(max_length=15)
    address = models.TextField()
    admission_date = models.DateField()
    status = models.CharField(max_length=20, default="active")