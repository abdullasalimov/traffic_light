from django.urls import path
from employee.views import index

urlpatterns = [
    path('', index, name='index'),
]