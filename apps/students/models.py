from django.db import models
from core.models import TimeStampedModel
from django.utils import timezone


class Student(TimeStampedModel):

    student_code = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )
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

    def save(self, *args, **kwargs):
        if not self.student_code:
            year = timezone.now().year
            prefix = f"ISC-{year}"
            last_student = Student.objects.filter(
                student_code__startswith=prefix
            ).order_by("student_code").last()
            
            if last_student:
                last_number = int(last_student.student_code.split("-")[-1])
                last_number = last_number + 1
            else:
                last_number = 1

            self.student_code = f"{prefix}-{last_number:03d}"
        super().save(*args, **kwargs)