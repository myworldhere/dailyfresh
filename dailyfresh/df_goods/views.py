# coding=utf-8
from django.shortcuts import render
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