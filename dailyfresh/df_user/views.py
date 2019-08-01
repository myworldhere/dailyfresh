# coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from models import *
from df_goods.models import *
from hashlib import sha1
import user_decorator


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


def login(request):
    name = request.COOKIES.get('name', '')
    context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 0, 'name': name}
    return render(request, 'df_user/login.html', context)


def login_handle(request):
    post = request.POST
    name = post.get('username')
    pwd = post.get('pwd')
    user_list = UserInfo.objects.filter(name=name)
    print post
    if len(user_list) == 1:
        s = sha1()
        s.update(pwd)
        s_pwd = s.hexdigest()
        if user_list[0].pwd == s_pwd:
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)
            save = post.get('save')
            if save == '1':
                red.set_cookie('name', name)
            else:
                red.set_cookie('name', '', max_age=-1)
            request.session['user_id'] = user_list[0].id
            request.session['user_name'] = name
            request.session.set_expiry(0)
            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'name': name, 'pwd': pwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'name': name, 'pwd': pwd}
        return render(request, 'df_user/login.html', context)


@user_decorator.login
def user_center_info(request):
    user_id = request.session['user_id']
    email = UserInfo.objects.get(id=user_id).email

    context = {'title': '用户中心', 'name': request.session['user_name'], 'page_style': 'user', 'email': email,
               'selected': 'info'}
    records = request.COOKIES.get('records')
    if records:
        records = records.split(',')
        goods_history = [GoodsInfo.objects.get(id=ID) for ID in records]
        print goods_history
        context['records'] = goods_history

    return render(request, 'df_user/user_center_info.html', context)


@user_decorator.login
def order(request):
    context = {'title': '用户中心', 'selected': 'order', 'page_style': 'user'}
    return render(request, 'df_user/user_center_order.html', context)


@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.consignee = post.get('consignee')
        user.postcode = post.get('postcode')
        user.address = post.get('address')
        user.phone = post.get('phone')
        user.save()
    context = {'title': '用户中心', 'selected': 'site', 'page_style': 'user', 'user': user}
    return render(request, 'df_user/user_center_site.html', context)


def logout(request):
    request.session.flush()
    return redirect('/')


