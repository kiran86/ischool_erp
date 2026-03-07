from django.db import models
from core.models import TimeStampedModel

# Create your models here.
class Enrollment(TimeStampedModel):

    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE
    )

    batch = models.ForeignKey(
        "courses.Batch",
        on_delete=models.CASCADE
    )

    enrollment_date = models.DateField()
    status = models.CharField(max_length=20)