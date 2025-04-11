from django.urls import path
from . import views

urlpatterns = [
 path('رزرو-نوبت/', views.create_appointment, name='create_appointment'),
    path('نوبت-های-من/', views.my_appointments, name='my_appointments'),
    path('نوبت/<int:appointment_id>/تایید/', views.update_appointment_status, {'action': 'confirm'}, name='confirm_appointment'),
    path('نوبت/<int:appointment_id>/رد/', views.update_appointment_status, {'action': 'reject'}, name='reject_appointment'),
]
