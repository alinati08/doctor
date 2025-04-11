from django.db import models
from user.models import User

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'در انتظار تأیید'),
        ('confirmed', 'تأیید شده'),
        ('rejected', 'رد شده'),
    )

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments', limit_choices_to={'role': 'user'}, verbose_name='بیمار')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments', limit_choices_to={'role': 'doctor'}, verbose_name='پزشک')
    date = models.DateField(verbose_name='تاریخ نوبت')
    time = models.TimeField(verbose_name='ساعت نوبت')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name='وضعیت')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')

    def __str__(self):
        return f"{self.patient.full_name} - {self.doctor.full_name} | {self.date} - {self.time}"

    class Meta:
        verbose_name = 'نوبت'
        verbose_name_plural = 'نوبت‌ها'