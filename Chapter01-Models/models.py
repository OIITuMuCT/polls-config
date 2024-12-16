from django.db import models


# Create your models here.
# Example model choices
class ModelName(models.Model):
    LIST = [
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    ]
    field_name = models.CharField(choices=LIST)
