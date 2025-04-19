from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('phone', 'full_name', 'role', 'is_active' , 'is_verified')
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('اطلاعات شخصی', {'fields': ('full_name', 'email', 'role', 'medical_license', 'specialty', 'is_verified')}),
        ('دسترسی‌ها', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('گروه‌ها و مجوزها', {'fields': ('groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('phone', 'full_name', 'password1', 'password2', 'role'),
        }),
    )
    search_fields = ('phone',)
    ordering = ('phone',)

admin.site.register(User, UserAdmin)
admin.site.site_header = 'مدیریت سایت'
admin.site.site_title = 'پنل ادمین'
admin.site.index_title = 'به پنل مدیریت خوش آمدید'