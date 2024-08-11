from django.db import models


class Employees(models.Model):
    DEPARTMENT_NAMES = (('Marketing', 'Marketing'),
                        ('Finance', 'Finance'),
                        ('Human Resources', 'Human Resources'),
                        ('Sales', 'Sales'),
                        ('IT', 'IT'))
    POSITIONS = (('Employees', 'Employees'),
                 ('Manager', 'Manager'),
                 ('Director', 'Director'),
                 ('Vice President', 'Vice President'),
                 ('CEO', 'CEO'))

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(choices=POSITIONS, max_length=50)
    department_name = models.CharField(choices=DEPARTMENT_NAMES, max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'