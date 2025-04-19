from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, DoctorRegisterForm, LoginForm ,DoctorAvailabilityForm
from django.contrib import messages
from .models import User ,DoctorAvailability
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory

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
    return render(request, 'user/register_user.html', {'form': form})

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
    return render(request, 'user/register_doctor.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.role == 'user':
                return redirect('user_dashboard')
            if not user.is_verified and user.role == 'doctor':
                messages.error(request, "اکانت شما هنوز توسط مدیریت تایید نشده است.")
                return redirect('login')
            elif user.is_verified and user.role == 'doctor':
                return redirect('doctor_dashboard')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

@login_required
def user_dashboard(request):
    return render(request, 'user/user_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'user/doctor_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def doctor_availability(request):
    if request.user.role != 'doctor':
        return redirect('login')

    AvailabilityFormSet = modelformset_factory(DoctorAvailability, form=DoctorAvailabilityForm, extra=1, can_delete=True)
    queryset = DoctorAvailability.objects.filter(doctor=request.user)

    if request.method == 'POST':
        formset = AvailabilityFormSet(request.POST, queryset=queryset)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.doctor = request.user
                instance.save()
            formset.save()
            messages.success(request, "زمان‌های کاری با موفقیت ذخیره شدند.")
            return redirect('doctor_availability')
    else:
        formset = AvailabilityFormSet(queryset=queryset)

    return render(request, 'user/doctor_availability.html', {'formset': formset})


def doctor_list(request):
    doctors = User.objects.filter(role='doctor', is_verified=True)
    return render(request, 'user/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(User, id=doctor_id, role='doctor', is_verified=True)
    availabilities = DoctorAvailability.objects.filter(doctor=doctor)
    return render(request, 'user/doctor_detail.html', {
        'doctor': doctor,
        'availabilities': availabilities,
    })
