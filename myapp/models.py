from django.db import models
# Create your models here.


class Listss(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    schoolNum = models.CharField(max_length=12, verbose_name='学号')
    grade = models.CharField(max_length=10, verbose_name='班级')


class Lists(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    schoolNum = models.CharField(max_length=12, verbose_name='学号')
    grade = models.CharField(max_length=10, verbose_name='班级')
class record(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    grade = models.CharField(max_length=10, verbose_name='班级')
    schoolNum = models.CharField(max_length=12, verbose_name='学号')
    # begin = models.CharField(max_length=100, verbose_name='请假开始时间')
    begin = models.DateTimeField(max_length=100, verbose_name='请假开始时间')
    # end = models.CharField(max_length=100, verbose_name='请假结束时间')
    end = models.DateTimeField(max_length=100, verbose_name='请假结束时间')
    # end = models.DateTimeField(max_length=100, verbose_name='请假结束时间')
    # why = models.CharField(max_length=1000, verbose_name='原因')
    why = models.TextField(verbose_name='原因')
    to = models.CharField(max_length=1000, verbose_name='去向')
    time = models.DateTimeField(verbose_name='请假时间')
    times = models.IntegerField(verbose_name='请假次数')
    flag = models.CharField(max_length=10, verbose_name='是否为最近一次请假')
