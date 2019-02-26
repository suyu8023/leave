# Generated by Django 2.1.1 on 2018-09-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qingjia', '0003_auto_20180912_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='record1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolNum', models.CharField(max_length=20, verbose_name='学号')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('grade', models.CharField(max_length=20, verbose_name='班级')),
                ('begin_time', models.CharField(max_length=30, verbose_name='请假开始时间')),
                ('end_time', models.CharField(max_length=30, verbose_name='请假结束时间')),
                ('why', models.CharField(max_length=1000, verbose_name='原因')),
                ('to', models.CharField(max_length=1000, verbose_name='去向')),
                ('last_time', models.DateTimeField(verbose_name='登录时间')),
                ('last_ip', models.CharField(max_length=20, verbose_name='登录ip')),
                ('lab', models.CharField(max_length=10, verbose_name='实验室')),
            ],
        ),
    ]