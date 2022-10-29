from django.contrib import admin
from employee.models import Department, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("fullname", 'job_title', 'employment_date', 'salary', 'department')