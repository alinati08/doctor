from django import template
import jdatetime
import datetime
register = template.Library()

@register.filter
def to_jalali(value):
    try:
        if isinstance(value, datetime.date):
            jalali_date = jdatetime.date.fromgregorian(date=value)
            return jalali_date.strftime('%Y/%m/%d')
        elif isinstance(value, datetime.datetime):
            jalali_date = jdatetime.datetime.fromgregorian(datetime=value)
            return jalali_date.strftime('%Y/%m/%d')
        else:
            return value
    except:
        return value

@register.filter
def persian_time(value):
    try:
        return value.strftime('%H:%M')
    except:
        return value