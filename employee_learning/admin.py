from django.contrib import admin

from .models import Employee
from .models import Division
from .models import PersonalInfo

# Register your models here.
admin.site.register(Employee)
admin.site.register(Division)
admin.site.register(PersonalInfo)