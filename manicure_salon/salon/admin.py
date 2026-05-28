from django.contrib import admin
from .models import Appointment, Master, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')
    search_fields = ('name',)


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience', 'specialization')
    search_fields = ('name', 'specialization')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'phone', 'service', 'date')
    search_fields = ('client_name', 'phone', 'service')
    list_filter = ('date', 'service')
