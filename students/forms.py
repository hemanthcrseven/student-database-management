from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "roll_number",
            "name",
            "age",
            "gender",
            "email",
            "phone",
            "city",
            "department",
            "year_of_study",
            "date_of_admission",
        ]
        widgets = {
            "date_of_admission": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply a common CSS class to every field for consistent styling
        for field_name, field in self.fields.items():
            existing = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (existing + " form-control").strip()


class StudentSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name, roll no, or city...", "class": "form-control"}
        ),
    )
    department = forms.ChoiceField(
        required=False,
        choices=[("", "All Departments")] + Student.DEPARTMENT_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
