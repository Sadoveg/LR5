from django.urls import path
from . import views

app_name = 'salon'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('masters/', views.masters, name='masters'),
    path('booking/', views.booking, name='booking'),
    path('contacts/', views.contacts, name='contacts'),
]
