from django.db import models
from django.urls import reverse


class Student(models.Model):
    DEPARTMENT_CHOICES = [
        ("CSE", "Computer Science & Engineering"),
        ("ECE", "Electronics & Communication Engineering"),
        ("EEE", "Electrical & Electronics Engineering"),
        ("MECH", "Mechanical Engineering"),
        ("CIVIL", "Civil Engineering"),
        ("IT", "Information Technology"),
        ("MBA", "Business Administration"),
        ("OTHER", "Other"),
    ]

    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    roll_number = models.CharField(
        max_length=20, unique=True, help_text="Unique roll / registration number"
    )
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100)
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)
    year_of_study = models.PositiveSmallIntegerField(
        default=1, help_text="Current year, e.g. 1-4"
    )
    date_of_admission = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.roll_number})"

    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk": self.pk})
