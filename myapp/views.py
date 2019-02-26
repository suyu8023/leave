import datetime,calendar
import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from myapp.models import record, Lists
from django.utils import timezone
# Create your views here.


def index(request):
    return render(request, 'index.html')


def post(request):
    # file = '/usr/SDUT.txt'
    # print(123456)
    # with open(file) as f:
        # line = f.readline()
        # while line:
            # print(line)
            # b = line.split('|')
             #print(b[0], b[1], b[5])
            # data = Lists()
            # data.name = b[1]
            # data.grade = b[5]
            # data.schoolNum = b[0]
            # data.save()
           #  line = f.readline()
       
    name = request.POST.get('name')
    xuehao = request.POST.get('xuehao')
    class1 = request.POST.get('class1')
    begin = request.POST.get('begin')
    end = request.POST.get('end')
    why = request.POST.get('why')
    to = request.POST.get('to')

    print(begin, end)
    # b = time.split('-')
    # print(b[0], b[1])
    if not (len(xuehao) == 11 and len(begin) == 16 and len(end) == 16 and len(why) >= 1 and len(to) >= 1):
        # messages.error(request, '输入的学号不正确')
        return render(request, 'error.html')
    else:
        data = record()
        data.name = name
        data.grade = class1
        data.schoolNum = xuehao
        data.begin = begin
        data.end = end
        data.why = why
        data.to = to
        data.times = 1
        data.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data.flag = ' '
        try:
            Lists.objects.get(name=data.name, schoolNum=data.schoolNum)
            try:
                b = record.objects.get(name=data.name, schoolNum=data.schoolNum, flag='请假次数')
                # print(b)
                data.times = b.times + 1
                data.flag = '请假次数'
                b.flag = ' '
                b.save()
            except:
                data.flag = '请假次数'
                # print("查询不到")
            data.save()
            print(name, xuehao, class1, begin, end, why, to)
            return render(request, 'success.html')
        except:
            return render(request, 'error.html')
