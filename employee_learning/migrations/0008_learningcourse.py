# Generated by Django 5.1.3 on 2024-12-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee_learning", "0007_personalinfo"),
    ]

    operations = [
        migrations.CreateModel(
            name="LearningCourse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, unique=True)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("B", "Basic"),
                            ("I", "Intermediate"),
                            ("A", "Advanced"),
                        ],
                        max_length=1,
                    ),
                ),
                ("employee", models.ManyToManyField(to="employee_learning.employee")),
            ],
        ),
    ]
