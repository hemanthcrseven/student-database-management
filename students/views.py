from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm, StudentSearchForm
from .models import Student


def student_list(request):
    students = Student.objects.all()
    search_form = StudentSearchForm(request.GET or None)

    if search_form.is_valid():
        query = search_form.cleaned_data.get("q")
        department = search_form.cleaned_data.get("department")

        if query:
            students = students.filter(
                Q(name__icontains=query)
                | Q(roll_number__icontains=query)
                | Q(city__icontains=query)
            )
        if department:
            students = students.filter(department=department)

    context = {
        "students": students,
        "search_form": search_form,
        "total_count": students.count(),
    }
    return render(request, "students/student_list.html", context)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/student_detail.html", {"student": student})


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f"Student '{student.name}' added successfully.")
            return redirect("student-list")
    else:
        form = StudentForm()
    return render(
        request, "students/student_form.html", {"form": form, "title": "Add Student"}
    )


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f"Student '{student.name}' updated successfully.")
            return redirect("student-list")
    else:
        form = StudentForm(instance=student)
    return render(
        request,
        "students/student_form.html",
        {"form": form, "title": f"Edit Student: {student.name}"},
    )


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        name = student.name
        student.delete()
        messages.success(request, f"Student '{name}' deleted successfully.")
        return redirect("student-list")
    return render(request, "students/student_confirm_delete.html", {"student": student})
