# coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse
from models import *
from hashlib import sha1
# Create your views here.


def register(request):
    return render(request, 'df_user/register.html', {'title': '注册'})


def register_handle(request):
    # 接受用户输入
    post = request.POST
    name = post.get('user_name')
    pwd = post.get('pwd')
    c_pwd = post.get('cpwd')
    email = post.get('email')
    print post
    # 判断两次密码
    if pwd != c_pwd:
        return redirect('/user/register/')

    # 创建对象
    user = UserInfo()
    user.name = name
    user.email = email
    # 面膜加密
    s = sha1()
    s.update(pwd)
    s_pwd = s.hexdigest()
    user.pwd = s_pwd
    user.save()
    # 注册成功，转到登录页面
    return redirect('/user/login/')


def register_exist(request):
    name = request.GET.get('name')
    print name
    count = UserInfo.objects.filter(name=name).count()
    print count
    return JsonResponse({'count': count})


