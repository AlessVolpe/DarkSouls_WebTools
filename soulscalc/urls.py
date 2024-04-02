from django.urls import path, include
from .views import *

urlpatterns = [
    path('', GamesView.as_view(), name='games'),
    path('calculator/', CalculatorView.as_view(), name='calculator')
]
