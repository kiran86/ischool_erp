from django.db import models
from core.models import TimeStampedModel

class Course(TimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration_months = models.IntegerField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)

class Batch(TimeStampedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch_code = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()
    teacher = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True
    )