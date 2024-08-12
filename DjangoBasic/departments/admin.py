from django.contrib import admin

from DjangoBasic.departments.models import Employees


# Register your models here.
@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    pass
