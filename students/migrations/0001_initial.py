from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("roll_number", models.CharField(help_text="Unique roll / registration number", max_length=20, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("age", models.PositiveIntegerField()),
                ("gender", models.CharField(blank=True, choices=[("M", "Male"), ("F", "Female"), ("O", "Other")], max_length=1)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("phone", models.CharField(blank=True, max_length=15)),
                ("city", models.CharField(max_length=100)),
                ("department", models.CharField(choices=[("CSE", "Computer Science & Engineering"), ("ECE", "Electronics & Communication Engineering"), ("EEE", "Electrical & Electronics Engineering"), ("MECH", "Mechanical Engineering"), ("CIVIL", "Civil Engineering"), ("IT", "Information Technology"), ("MBA", "Business Administration"), ("OTHER", "Other")], max_length=10)),
                ("year_of_study", models.PositiveSmallIntegerField(default=1, help_text="Current year, e.g. 1-4")),
                ("date_of_admission", models.DateField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]
