from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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
    specialty = models.CharField(max_length=100, blank=True, null=True, verbose_name="تخصص")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'