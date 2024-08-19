from django.urls import path

from . import views
from .views import calculate_souls

urlpatterns = [
    path('', views.calculator_form, name='calculator_form'),
    path('calculate_souls/', calculate_souls, name='calculate_souls'),
]
