from django.db import models
from core.models import TimeStampedModel

# Create your models here.
class Attendance(TimeStampedModel):

    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE
    )

    batch = models.ForeignKey(
        "courses.Batch",
        on_delete=models.CASCADE
    )

    date = models.DateField()
    status = models.CharField(max_length=10)

    marked_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True
    )