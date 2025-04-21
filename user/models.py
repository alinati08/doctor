from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MedicalMajor(models.Model):
    title = models.CharField("عنوان تخصص", max_length=100)

    class Meta:
        verbose_name = 'تخصص'
        verbose_name_plural = 'تخصص‌ها'

    def __str__(self):
        return self.title



class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("کاربر باید شماره تلفن داشته باشد")
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('user', 'کاربر'),
        ('doctor', 'پزشک'),
    )
    
    phone = models.CharField(max_length=11, unique=True, verbose_name="شماره تلفن")
    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(null=True, blank=True, verbose_name="ایمیل")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user', verbose_name="نقش")
    
    # Fields for doctors only
    medical_license = models.CharField(max_length=100, blank=True, null=True, verbose_name="شماره نظام پزشکی")
    specialty = models.ForeignKey(MedicalMajor, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="تخصص")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False, verbose_name="تایید شده توسط ادمین")

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        
class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'doctor'}, verbose_name="پزشک")
    day_of_week = models.CharField(
        max_length=10,
        choices=[
            ('شنبه', 'شنبه'),
            ('یکشنبه', 'یکشنبه'),
            ('دوشنبه', 'دوشنبه'),
            ('سه‌شنبه', 'سه‌شنبه'),
            ('چهارشنبه', 'چهارشنبه'),
            ('پنجشنبه', 'پنجشنبه'),
            ('جمعه', 'جمعه'),
        ],
        verbose_name="روز هفته"
    )
    start_time = models.TimeField(verbose_name="شروع")
    end_time = models.TimeField(verbose_name="پایان")

    class Meta:
        verbose_name = 'زمان کاری پزشک'
        verbose_name_plural = 'زمان‌های کاری پزشکان'

    def __str__(self):
        return f"{self.doctor.full_name} - {self.day_of_week} ({self.start_time} تا {self.end_time})"
    
    
