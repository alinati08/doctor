from django import forms
from .models import Appointment
from user.models import User

class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=User.objects.filter(role='doctor'), label='پزشک')

    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'description']
        widgets = {
            'date': forms.TextInput(attrs={'id': 'id_date'}),  # مهم!
            'time': forms.TextInput(attrs={'id': 'id_time'}),
        }
        labels = {
            'date': 'تاریخ',
            'time': 'ساعت',
            'description': 'توضیحات',
        }