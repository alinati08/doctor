from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User , DoctorAvailability

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='رمز عبور')

    class Meta:
        model = User
        fields = ['phone', 'full_name', 'email', 'password']

class DoctorRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='رمز عبور')

    class Meta:
        model = User
        fields = ['phone', 'full_name', 'email', 'password', 'medical_license', 'specialty']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="شماره تلفن")
    password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")


class DoctorAvailabilityForm(forms.ModelForm):
    class Meta:
        model = DoctorAvailability
        fields = ['day_of_week', 'start_time', 'end_time']
        labels = {
            'day_of_week': 'روز هفته',
            'start_time': 'ساعت شروع',
            'end_time': 'ساعت پایان',
        }
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }