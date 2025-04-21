from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Appointment
from django.shortcuts import get_object_or_404
from django.contrib import messages
from persiantools.jdatetime import JalaliDate
from datetime import datetime
import jdatetime
from datetime import date

def convert_persian_to_gregorian(persian_str):
    persian_str = ''.join([str("۰۱۲۳۴۵۶۷۸۹".index(c)) if c in "۰۱۲۳۴۵۶۷۸۹" else c for c in persian_str])
    year, month, day = map(int, persian_str.split('-'))
    j_date = jdatetime.date(year, month, day)
    g_date = j_date.togregorian()
    return g_date

@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            persian_date_str = request.POST.get('date')
            appointment.date = convert_persian_to_gregorian(persian_date_str)
            appointment.save()
            return redirect('my_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'reservation/create_appointment.html', {'form': form})

@login_required
def my_appointments(request):
    if request.user.role == 'user':
        appointments = Appointment.objects.filter(patient=request.user)
    elif request.user.role == 'doctor':
        appointments = Appointment.objects.filter(doctor=request.user)
    else:
        appointments = []
    return render(request, 'reservation/my_appointments.html', {'appointments': appointments})

@login_required
def update_appointment_status(request, appointment_id, action):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.user != appointment.doctor:
        messages.error(request, "شما اجازه دسترسی به این نوبت را ندارید.")
        return redirect('my_appointments')

    if action == 'confirm':
        appointment.status = 'confirmed'
        messages.success(request, 'نوبت تأیید شد.')
    elif action == 'reject':
        appointment.status = 'rejected'
        messages.warning(request, 'نوبت رد شد.')
    appointment.save()
    return redirect('my_appointments')

