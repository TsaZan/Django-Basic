import time

from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(f"Response: {time.time()} ")


def department_by_id(request, pk):
    return HttpResponse(f"Department ID: {pk}")

def department_by_name(request, name):
    return HttpResponse(f"Department Name: {name}")
