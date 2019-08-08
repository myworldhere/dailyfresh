# coding=utf-8
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from models import *
from df_user import user_decorator
from df_user.models import *
from df_goods.models import *
# Create your views here.


@user_decorator.login
def cart(request):
    user_id = request.session.get('user_id')
    array = CartInfo.objects.filter(user_id=user_id)
    context = {'title': '购物车', 'page_style': 'user', 'carts': array}
    return render(request, 'df_cart/cart.html', context)


def cart_count(request):
    try:
        user_id = request.session.get('user_id')
        array = CartInfo.objects.filter(user_id=user_id)
        data = {'status': 0, 'count': len(array)}
    except Exception as e:
        data = {'status': 1, 'error': e}

    return JsonResponse(data)


@user_decorator.login
def add_cart(request, goods_id, count):
    user_id = request.session.get('user_id')
    carts = CartInfo.objects.filter(goods_id=goods_id, user_id=user_id)
    if carts:
        cart = carts[0]
        cart.count = cart.count + int(count)
    else:
        cart = CartInfo()
        goods = GoodsInfo.objects.get(id=goods_id)
        user = UserInfo.objects.get(id=user_id)
        cart.goods = goods
        cart.count = count
        cart.user = user
    cart.save()

    if request.is_ajax():
        return JsonResponse({'status': 0})
    else:
        return redirect('/'+goods_id)


@user_decorator.login
def del_carts(request, ID):
    try:
        CartInfo.objects.filter(id=ID).delete()
        data = {'status': 0}
    except Exception as e:
        data = {'status': 1}
    return JsonResponse(data)


@user_decorator.login
def edit(request, cart_id, count):
    try:
        cart = CartInfo.objects.get(id=cart_id)
        count1 = int(count)
        cart.count = count
        cart.save()
        data = {'status': 0}
    except Exception as e:
        data = {'status': count1}
    return JsonResponse(data)