# coding=utf-8
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from models import *
from df_cart.models import *
from django.db import transaction
from df_user import user_decorator
from datetime import datetime
from decimal import Decimal
from df_user.models import *
# Create your views here.


@user_decorator.login
def place_order(request):

    cart_ids = request.GET.get('ids')
    ids = cart_ids.split(',')

    array = [CartInfo.objects.get(id=x) for x in ids]
    user_id = request.session.get('user_id')

    user = UserInfo.objects.get(id=user_id)

    context = {'title': '创建订单', 'page_style': 'user', 'carts': array, "name": user.name, 'phone': user.phone, 'address': user.address}
    return render(request, 'df_order/place_order.html', context)


def handle_cart(request):
    params = request.GET.get('cart_ids')
    return JsonResponse({'status': 0, 'data': params})


"""
事务：一旦操作失败，则全部回退
1.创建订单对象
2.判断商品库存
3.创建详单对象
4.修改商品库存
5.删除购物车

"""


@transaction.atomic()
@user_decorator.login
def create_order(request):
    tran_id = transaction.savepoint()
    cart_ids = request.POST.get('cart_ids')  # 5,6
    try:
        # 创建订单
        print 0
        order = OrderInfo()
        now = datetime.now()
        user_id = request.session.get('user_id')
        order.id = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), user_id)
        order.user_id = user_id
        order.date = now
        order.total = Decimal(request.POST.get('total'))
        order.save()
        print 1
        # 创建详单对象
        carts_array = [int(x) for x in cart_ids.split(',')]
        for ID in carts_array:
            print ID
            detail = OrderDetailInfo()
            detail.order = order
            # 查询购物车信息
            cart = CartInfo.objects.get(id=ID)
            # 判断库存
            goods = cart.goods
            if goods.inventory >= cart.count:  # 如果库存大于购买数量
                # 减少商品库存
                goods.inventory = goods.inventory - cart.count
                goods.save()
                # 完善详单信息
                detail.goods_id = goods.id
                detail.price = goods.price
                detail.count = cart.count
                detail.save()
                print 2
                # 删除购物车数据
                cart.delete()
            else:  # 如果库存小于购买数量
                print 3
                data = {'status': 1, 'res': '库存不足'}
                transaction.savepoint_rollback(tran_id)
                return JsonResponse(data)
        # 确认事务完成
        transaction.savepoint_commit(tran_id)
        data = {'status': 0, 'res': '创建成功'}
    except Exception as e:
        print 5
        data = {'status': 1, 'res': e}
        transaction.savepoint_rollback(tran_id)
    print 6
    return JsonResponse(data)