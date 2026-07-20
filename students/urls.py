from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name="student-list"),
    path("student/add/", views.student_create, name="student-add"),
    path("student/<int:pk>/", views.student_detail, name="student-detail"),
    path("student/<int:pk>/edit/", views.student_update, name="student-edit"),
    path("student/<int:pk>/delete/", views.student_delete, name="student-delete"),
]
