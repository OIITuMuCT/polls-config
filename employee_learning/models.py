from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.id}: {self.name}'

class Division(models.Model):
    div_name = models.CharField(max_length=25)
    in_scope = models.BooleanField(help_text='If the division is target for the learning program, check this filed.')

    def __str__(self):
        return self.div_name

# Example model choices
class ModelName(models.Model):
    LIST = [('H', 'High'), ('M', 'Medium'), ('L', 'Low'),]
    field_name = models.CharField(choices=LIST)