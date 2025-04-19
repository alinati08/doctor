from django.urls import path
from . import views

urlpatterns = [
    path('ثبت-نام-کاربر/', views.register_user, name='register_user'),
    path('ثبت-نام-پزشک/', views.register_doctor, name='register_doctor'),
    path('ورود/', views.login_view, name='login'),
    path('خروج/', views.logout_view, name='logout'),
    path('داشبورد-کاربر/', views.user_dashboard, name='user_dashboard'),
    path('داشبورد-پزشک/', views.doctor_dashboard, name='doctor_dashboard'),
    path('تنظیم-زمان-کاری/', views.doctor_availability, name='doctor_availability'),
]