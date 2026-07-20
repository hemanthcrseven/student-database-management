from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("roll_number", "name", "age", "department", "city", "year_of_study")
    list_filter = ("department", "year_of_study", "gender")
    search_fields = ("name", "roll_number", "city", "email")
    ordering = ("name",)
