from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User ,MedicalMajor ,DoctorAvailability
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
import pdfkit

class UserAdmin(BaseUserAdmin):
    list_display = ('phone', 'full_name', 'role', 'is_active' , 'is_verified')
    actions = ['export_users_list_pdf']
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
    def export_users_list_pdf(self, request, queryset):
        if queryset.count() == 0:
            self.message_user(request, "هیچ کاربری انتخاب نشده.", level='error')
            return

        html = render_to_string('user_pdf_template.html', {
            'users': list(queryset),
        })

        config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

        options = {
            'enable-local-file-access': '',
            'encoding': 'UTF-8',
            'quiet': '',
            'page-size': 'A4',
            'margin-top': '10mm',
            'margin-bottom': '10mm',
            'margin-left': '10mm',
            'margin-right': '10mm',
            'dpi': 400,
            'zoom': 1,
        }
        pdf = pdfkit.from_string(html, False, options=options, configuration=config)

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=users_list.pdf'
        return response

    export_users_list_pdf.short_description = "📄 خروجی PDF لیست کاربران انتخابی"


class DoctorAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'day_of_week', 'start_time', 'end_time')
    actions = ['export_availabilities_pdf']

    def export_availabilities_pdf(self, request, queryset):
        if queryset.count() == 0:
            self.message_user(request, "هیچ رکوردی انتخاب نشده.", level='error')
            return

        html = render_to_string('availability_pdf_template.html', {
            'availabilities': list(queryset),
        })

        config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

        options = {
            'enable-local-file-access': '',
            'encoding': 'UTF-8',
            'quiet': '',
            'page-size': 'A4',
            'margin-top': '10mm',
            'margin-bottom': '10mm',
            'margin-left': '10mm',
            'margin-right': '10mm',
            'dpi': 400,
            'zoom': 1,
        }

        pdf = pdfkit.from_string(html, False, options=options, configuration=config)

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=availabilities.pdf'
        return response

    export_availabilities_pdf.short_description = "📄 خروجی PDF زمان‌های کاری انتخابی"

admin.site.register(User, UserAdmin)
admin.site.register(MedicalMajor)
admin.site.register(DoctorAvailability, DoctorAvailabilityAdmin)
admin.site.site_header = 'مدیریت سایت'
admin.site.site_title = 'پنل ادمین'
admin.site.index_title = 'به پنل مدیریت خوش آمدید'