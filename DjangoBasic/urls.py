"""
URL configuration for DjangoBasic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from DjangoBasic.departments.views import index, department_by_id, department_by_name, show_departments_and_ids

urlpatterns = [
    path('admin/', admin.site.urls),
    path('departments/', include('DjangoBasic.departments.urls')),
    path('<employee_id>', show_departments_and_ids),

]
