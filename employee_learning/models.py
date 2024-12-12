from django.db import models

# Create your models here.
class Employee(models.Model):
    PRIORITIES = [('H', 'High'), ('M', 'Medium'), ('L', 'Low'),]
    name = models.CharField(max_length=25, verbose_name="Employee Name")

    def __str__(self):
        return f'{self.id}: {self.name}'

class Division(models.Model):
    div_name = models.CharField(max_length=25)
    in_scope = models.BooleanField(help_text='If the division is target for the learning program, check this filed.')

    def __str__(self):
        return self.div_name
