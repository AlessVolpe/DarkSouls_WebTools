from django.urls import path

from . import views
from .views import calculate_souls2

urlpatterns = [
    path('', views.calculator_form2, name='calculator_form2'),
    path('calculate_souls2/', calculate_souls2, name='calculate_souls2'),
]