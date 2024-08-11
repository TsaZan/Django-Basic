import time
from django.http import HttpResponse
from django.shortcuts import render

from DjangoBasic.departments.models import Employees


# Create your views here.
def index(request, *args, **kwargs):
    content = (f"Response: {time.time()}</br>"
               f"User = {request.user}")
    return HttpResponse(content)


def department_by_id(request, pk):
    content = f"Department ID: {pk}"
    return HttpResponse(content)


def department_by_name(request, name):
    content = f"Department Name: {name}"
    return HttpResponse(content)


def show_departments_and_ids(request, employee_id):
    employee = Employees.objects.all().filter(pk=employee_id).first()

    content = {"department_name": employee.department_name,
               "position": employee.position,
               "employees_first_name": employee.first_name,
               "employees_last_name": employee.last_name,
               "logged": request.user,
               "id": employee.pk}
    return render(request=request,
                  template_name="show_departments_and_ids.html",
                  context=content)


def show_all_employees(request, name=''):

    all_employees = Employees.objects.all().order_by('id').filter(first_name__icontains=name)
    load = {'employees': all_employees}
    return render(request, 'show_all_employees.html', context=load)
