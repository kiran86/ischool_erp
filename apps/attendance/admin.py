from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "batch",
        "date",
        "status"
    )

    list_filter = ("batch", "date")