from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'date', 'time']
    list_filter = ['date', 'doctor']
    search_fields = ['patient__full_name', 'doctor__full_name']
