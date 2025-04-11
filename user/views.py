from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, DoctorRegisterForm, LoginForm
from .models import User
from django.contrib.auth.decorators import login_required

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'user'
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register_user.html', {'form': form})

def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.role = 'doctor'
            doctor.set_password(form.cleaned_data['password'])
            doctor.save()
            return redirect('login')
    else:
        form = DoctorRegisterForm()
    return render(request, 'accounts/register_doctor.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.role == 'user':
                return redirect('user_dashboard')
            elif user.role == 'doctor':
                return redirect('doctor_dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_dashboard(request):
    return render(request, 'accounts/user_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
