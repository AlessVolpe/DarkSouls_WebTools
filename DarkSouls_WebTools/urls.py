"""
URL configuration for DarkSouls_WebTools project.

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
from django.urls import include, path
from django.conf.urls import handler404, handler500

from . import views

handler404 = 'DarkSouls_WebTools.views.error_404'
handler500 = 'DarkSouls_WebTools.views.error_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('calculator_ds3/', include('calculator_ds3.urls')),
    path('about/', views.about, name='about'),
    path('404/', views.error_404, name='error_404'),
]
