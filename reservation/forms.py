from django import forms
from .models import Appointment
from user.models import User

class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=User.objects.filter(role='doctor'), label='پزشک')

    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'date': 'تاریخ',
            'time': 'ساعت',
            'description': 'توضیحات',
        }
