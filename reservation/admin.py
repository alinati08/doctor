from django.template.loader import render_to_string
from django.http import HttpResponse
import pdfkit
from .models import Appointment
from django.contrib import admin

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'date', 'time']
    list_filter = ['date', 'doctor']
    search_fields = ['patient__full_name', 'doctor__full_name']
    actions = ['export_appointments_pdf']

    def export_appointments_pdf(self, request, queryset):
        if queryset.count() == 0:
            self.message_user(request, "هیچ نوبتی انتخاب نشده.", level='error')
            return

        html = render_to_string('appointment_pdf_template.html', {
            'appointments': list(queryset),
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
        response['Content-Disposition'] = 'attachment; filename=appointments.pdf'
        return response

    export_appointments_pdf.short_description = "📄 خروجی PDF لیست نوبت‌های انتخابی"
