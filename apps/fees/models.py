from django.db import models
from core.models import TimeStampedModel

# Create your models here.
class Payment(TimeStampedModel):

    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE
    )

    enrollment = models.ForeignKey(
        "enrollment.Enrollment",
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100, blank=True)