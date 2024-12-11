from django.contrib import admin

from .models import Employee
from .models import Division

# Register your models here.
admin.site.register(Employee)
admin.site.register(Division)
