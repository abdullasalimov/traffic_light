from django.shortcuts import render
from employee.models import Department, Employee

def index(request):
    context = {}
    context['employee'] = Employee.objects.all()
    context['departments'] = Department.objects.all()
    context['departments_first'] = Department.objects.filter(level='1')
    context['departments_second'] = Department.objects.filter(level='2')
    context['departments_third'] = Department.objects.filter(level='3')
    context['departments_fourth'] = Department.objects.filter(level='4')
    context['departments_fifth'] = Department.objects.filter(level='5')

    return render(request, 'index.html', context=context)