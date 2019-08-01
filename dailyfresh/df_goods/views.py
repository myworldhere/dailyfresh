# coding=utf-8
from django.shortcuts import render
from django.core.paginator import Paginator
from models import *


# Create your views here.


def index(request):
    category_list = Category.objects.all()
    array = []
    for category in category_list:
        news = category.goodsinfo_set.order_by('-id')[0:4]
        hots = category.goodsinfo_set.order_by('-click')[0:4]
        array.append({'news': news, 'hots': hots, 'category': category})

    context = {'page_style': 'goods', 'title': '首页', 'array': array}
    return render(request, 'df_goods/index.html', context)


def list(request, tid, index, sort):
    category = Category.objects.get(id=tid)
    # 新品推荐
    news = category.goodsinfo_set.order_by('-id')[0:2]
    if sort == '1':  # 默认 上架时间排序
        goods_list = GoodsInfo.objects.filter(category_id=int(tid)).order_by('-id')
    elif sort == '2':  # 价格排序
        goods_list = GoodsInfo.objects.filter(category_id=int(tid)).order_by('-price')
    elif sort == '3':  # 人气，点击量排序
        goods_list = GoodsInfo.objects.filter(category_id=int(tid)).order_by('-click')

    paginator = Paginator(goods_list, 3)
    page = paginator.page(int(index))
    context = {
        'title': category.title,
        'page_style': 'goods',
        'page': page,
        'news': news,
        'sort': sort,
        'category': category,
        'paginator': paginator,
        'sort_title': ['默认', '价格', '人气']
    }
    return render(request, 'df_goods/list.html', context)


def detail(request, id):
    goods = GoodsInfo.objects.get(id=id)
    news = goods.category.goodsinfo_set.order_by('-id')[0:2]
    goods.click = goods.click + 1
    goods.save()
    context = {'title': goods.category.title, 'page_style': 'goods', 'goods': goods, 'news': news}
    response = render(request, 'df_goods/detail.html', context)
    # 最近浏览记录
    records = request.COOKIES.get('records', '')
    if records != '':
        records_array = records.split(',')
        if records_array.count(id) >= 1:  # 商品已记录则删除
            records_array.remove(id)
        records_array.insert(0, id)  # 添加到首位
        if len(records_array) > 5:  # 记录个数超过5个，删除尾部元素
            records_array.pop(5)
        records = ','.join(records_array)  # 拼接成字符串
    else:
        records = id

    response.set_cookie('records', records)
    return response
