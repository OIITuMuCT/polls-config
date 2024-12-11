from django.db import models

# Create your models here.
class ModelName(models.Model):
    field_name = models.FieldType(option)
    
# example:

class PetModel(models.Model):
    pet_name = models.CharField(max_length=20)