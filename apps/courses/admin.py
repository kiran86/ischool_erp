from django.contrib import admin
from .models import Course, Batch

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "duration_months",
        "fee"
    )

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):

    list_display = (
        "batch_code",
        "course",
        "start_date",
        "end_date",
        "capacity"
    )

    list_filter = ("course",)