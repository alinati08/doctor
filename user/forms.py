from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User

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
