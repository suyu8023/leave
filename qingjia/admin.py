from django.contrib import admin
from .models import record
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin
from .resources import CustomerResource1
from daterange_filter.filter import DateRangeFilter
admin.site.site_header = 'SDUTACM请假后台管理'
# Register your models here.
# from .models import user
# @admin.register(user)
# class user_list(admin.ModelAdmin):
#     list_display = ['account']


class CustomerAdmin1(ImportExportActionModelAdmin, ImportExportModelAdmin):
    list_display = ['id', 'schoolNum', 'name', 'grade', 'lab', 'begin_time', 'end_time', 'why', 'to', 'last_time',
                    'last_ip']
    search_fields = ['id', 'schoolNum', 'name', 'grade', 'lab']
    # list_display_links = ('schoolNum', 'grade')
    # list_editable = ['schoolNum']
    ordering = ['id']
    list_per_page = 30
    list_filter = (
        'grade',
        'lab',
        # 'last_time',
        ('last_time', DateRangeFilter),
    )
    resource_class = CustomerResource1

    # def has_add_permission(self, request):
    #     return False


admin.site.register(record, CustomerAdmin1)
