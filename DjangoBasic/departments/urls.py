from django.urls import path

from DjangoBasic.departments.views import department_by_id, department_by_name

urlpatterns = [
    path('<int:pk>/', department_by_id),
    path('<str:name>/', department_by_name)
]
