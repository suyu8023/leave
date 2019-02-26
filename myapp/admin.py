from django.contrib import admin
from .models import record, Lists
from daterange_filter.filter import DateRangeFilter
# Register your models here.


@admin.register(record)
class LeavesAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade', 'schoolNum', 'begin', 'end', 'why', 'to', 'time', 'times']
    search_fields = ['name', 'grade', 'schoolNum']
    date_hierarchy = 'begin'  # 详细时间分层筛选
    list_per_page = 30
    list_filter = (
        'grade',
        'flag',
        ('begin', DateRangeFilter),  # this is a tuple
    )


@admin.register(Lists)
class LeavesAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade', 'schoolNum']
    search_fields = ['name', 'grade', 'schoolNum']
    list_per_page = 30
    list_filter = (
        'grade',
    )
