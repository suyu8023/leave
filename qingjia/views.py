import time

import requests
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import record
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
import json
# Create your views here.


def index(request):
    request.session.set_expiry(1)
    return render(request, 'index.html')


def post(request):
    if request.method == 'POST':
        acc = request.POST['name']
        password = request.POST['password']
        url = "http://acm.sdut.edu.cn/onlinejudge2/index.php/API/Login?user_name="
        url = url + acc
        url = url + '&password='
        url = url + password
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r = json.loads(r.text, encoding='utf-8')
        if len(r):
            request.session['acc'] = acc
            request.session['pas'] = password
            return render(request, 'leave.html')
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'leave.html')


def post_info(request):
    acc = request.session.get('acc')
    if acc is None:
        return render(request, 'error.html')
    pas = request.session.get('pas')
    name = request.POST.get('name')
    grade = request.POST.get('grade')
    begin_time = request.POST.get('begin_time')
    end_time = request.POST.get('end_time')
    why = request.POST.get('why')
    to = request.POST.get('to')
    lab = request.POST.get('lab')
    url = "http://acm.sdut.edu.cn/onlinejudge2/index.php/API/Login?user_name="
    url = url + acc
    url = url + '&password='
    url = url + pas
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r = json.loads(r.text, encoding='utf-8')
    if len(r):
         # if r[0]['nick_name'][8:11] == name and r[0]['class'][0:6] == grade:
        try:
            i = r[0]['nick_name'].index(name)
            if r[0]['nick_name'][i:] == name:
                    i = r[0]['class'].find('(')
                    if i == -1:
                        class1 = r[0]['class']
                        # print(class1)
                    else:
                        class1 = r[0]['class'][:i]
                        # print(class1)
                    if class1 == grade:
                        if not (len(why) >= 1 and len(to) >= 1):
                            request.session['acc'] = acc
                            return render(request, 'error_2.html')
                        elif lab == "实验室":
                            return render(request, 'error_5.html')
                        else:
                            data = record()
                            data.name = name
                            data.schoolNum = acc
                            data.grade = grade
                            data.begin_time = begin_time
                            data.end_time = end_time
                            data.why = why
                            data.to = to
                            data.lab = lab
                            data.last_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                            str1 = begin_time[0:10]
                            str2 = begin_time[11:13]
                            str3 = begin_time[14:19]
                            str4 = end_time[0:10]
                            str5 = end_time[11:13]
                            str6 = end_time[14:19]
                            if str1 > str4:
                                return render(request, 'error_3.html')
                            elif str1 == str4:
                                if str2 == str5:
                                    if str3 >= str6:
                                        return render(request, 'error_3.html')
                                else:
                                    if str2 == "早上" and str5 == "凌晨":
                                        return render(request, 'error_3.html')
                                    elif str2 == "下午" and str5 == "凌晨":
                                        return render(request, 'error_3.html')
                                    elif str2 == "下午" and str5 == "早上":
                                        return render(request, 'error_3.html')
                                    elif str2 == "晚上" and str5 == "凌晨":
                                        return render(request, 'error_3.html')
                                    elif str2 == "晚上" and str5 == "下午":
                                        return render(request, 'error_3.html')
                                    elif str2 == "晚上" and str5 == "早上":
                                        return render(request, 'error_3.html')
                            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                            if x_forwarded_for:
                                ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
                            else:
                                ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
                            data.last_ip = ip
                            data.save()
                            return render(request, 'success.html')
                    else:
                        return render(request, 'error_1.html')
            else:
                return render(request, 'error_1.html')
        except:
            return render(request, 'error_1.html')
    else:
        return render(request, 'error_1.html')


@login_required
def myview(request):
    return render_to_response('index.html')

