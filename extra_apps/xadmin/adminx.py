from __future__ import absolute_import
import xadmin
from xadmin import views
from extra_apps import xadmin
from .models import UserSettings, Log
from myapp.models import Lists, record
from xadmin.layout import *

from django.utils.translation import ugettext_lazy as _, ugettext

class UserSettingsAdmin(object):
    model_icon = 'fa fa-cog'
    hidden_menu = True

xadmin.site.register(UserSettings, UserSettingsAdmin)

class LogAdmin(object):

    def link(self, instance):
        if instance.content_type and instance.object_id and instance.action_flag != 'delete':
            admin_url = self.get_admin_url('%s_%s_change' % (instance.content_type.app_label, instance.content_type.model), 
                instance.object_id)
            return "<a href='%s'>%s</a>" % (admin_url, _('Admin Object'))
        else:
            return ''
    link.short_description = ""
    link.allow_tags = True
    link.is_column = False

    list_display = ('action_time', 'user', 'ip_addr', '__str__', 'link')
    list_filter = ['user', 'action_time']
    search_fields = ['ip_addr', 'message']
    model_icon = 'fa fa-cog'

xadmin.site.register(Log, LogAdmin)



class GlobalSetting(object):
    # 设置base_site.html的Title
    site_title = '2018 ACM暑假集训请假'
    # 设置base_site.html的Footer
    site_footer = '2018 ACM暑假集训请假'


xadmin.site.register(views.CommAdminView, GlobalSetting)


class EmailVerifyRecordAdmin(object):
    list_display = ['name', 'schoolNum', 'grade', 'begin', 'end', 'why', 'to', 'time', 'times']
    search_fields = ['name', 'schoolNum']
    list_filter = ['begin', 'flag', 'grade']
    # model_icon = 'fa fa-address-book-o'


class BannerAdmin(object):
    list_display = ['name', 'schoolNum', 'grade']
    search_fields = ['name', 'schoolNum']
    # list_filter = ['title', 'image', 'url', 'index', 'add_time']


# from django.contrib.auth.models import User
xadmin.site.register(record, EmailVerifyRecordAdmin)
xadmin.site.register(Lists, BannerAdmin)
