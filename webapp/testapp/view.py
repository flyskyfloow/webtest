# 处理用户发出的请求，从 urls.py 中对应过来, 通过渲染 templates 中的网页可以将显示内容，比如登陆后的用户名，用户请求的数据，输出到网页。
import os
from django.shortcuts import render, render_to_response, redirect
# 导入models.py 中数据模型对应的类
from testapp.models import *
import json
from django.http import HttpResponse, HttpResponseRedirect
import socket
# 导入form 对应的类 用于数据检查
from testapp.forms import *
# 作用是跳过 csrf 中间件的保护
from django.views.decorators.csrf import csrf_exempt


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)


# 返回一个列表
def test(request):
    test_list = Person.objects.filter(first_name='guo')
    return render(request, "test.html", {'test_list': test_list})


# 展示所有的 request.META  数据
def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


# 提交表单
def search_form(request):
    return render_to_response('test.html')


# 获取提交值
# def search(request):
#     if 'q' in request.GET:
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)

# 查询解结果返回到页面
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        test_list = Person.objects.filter(first_name=q)
        return render(request, "test.html", {'test_list': test_list})
    else:
        return render_to_response('test.html', {'error': True})


# commit date to mysql
def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == 'POST':
        person_form = PersonForm(request.POST)
        if person_form.is_valid():
            person = Person()
            print(request.POST.get('first_name'))
            print(request.POST.get('last_name'))
            person.first_name = request.POST.get('first_name')
            person.last_name = request.POST.get('last_name')
            # save date to mysql
            person.save()
            return render(request, "welcome.html")
        else:
            print("测试失败")

# api 测试用例
def add_args(a, b):
    return a + b


# 接口函数 使用api的方式上传数据到数据库
def post(request):
    if request.method == 'POST':  # 当提交表单时
        dic = {}
        # 判断是否传参
        if request.POST:
            a = request.POST.get('a', 0)
            b = request.POST.get('b', 0)
            # 判断参数中是否含有a和b
            if a and b:
                res = add_args(a, b)
                dic['number'] = res
                dic = json.dumps(dic)
                person = Person()
                person.first_name = a
                person.last_name = b
                person.save()
                return HttpResponse(dic)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')

    else:
        return HttpResponse('方法错误')


# 执行系统命令
def run_cmd(request):
    if request.method == "GET":
        return render(request, "runcmd.html")
    elif request.method == "POST":
        print("this is a post request")
        web_cmd = request.POST.get("cmd")
        print(web_cmd)
        rsp = []
        for i in os.popen("dir").read():
            rsp.append(i)
        print(rsp)
        return HttpResponse("运行成功 主机名称 " + str(rsp ))


