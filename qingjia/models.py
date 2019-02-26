from django.db import models

# Create your models here.

#
# class user(models.Model):
#     username = models.CharField(max_length=20, verbose_name='账号')
#     password = models.CharField(max_length=20, verbose_name='密码')
#     nickname = models.CharField(max_length=20, verbose_name='昵称')
#     lasttime = models.DateTimeField(verbose_name='最后登录时间')
#     lastip = models.CharField(max_length=20, verbose_name='最后登录ip')

from django.db import models

# Create your models here.


class record(models.Model):
    schoolNum = models.CharField(max_length=20, verbose_name='学号')
    name = models.CharField(max_length=100, verbose_name='姓名')
    grade = models.CharField(max_length=20, verbose_name='班级')
    begin_time = models.CharField(max_length=30, verbose_name='请假开始时间')
    end_time = models.CharField(max_length=30, verbose_name='请假结束时间')
    why = models.TextField(verbose_name='原因')
    to = models.CharField(max_length=1000, verbose_name='去向')
    last_time = models.DateTimeField(verbose_name='登录时间')
    last_ip = models.CharField(max_length=20, verbose_name='登录ip')
    lab = models.CharField(max_length=10, verbose_name='实验室')

    def __str__(self):
        if len(str(self.why))>15:
            return '{0}......'.format(str(self.why)[0:15])
        else:
            return str(self.why)

