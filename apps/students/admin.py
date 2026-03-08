from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "student_code",
        "first_name",
        "last_name",
        "phone",
        "admission_date",
        "status"
    )

    readonly_fields = ("student_code",)

    search_fields = (
        "student_code",
        "first_name",
        "last_name",
        "phone"
    )

    list_filter = ("status",)