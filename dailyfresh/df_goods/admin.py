from django.contrib import admin
from models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'unit', 'click', 'inventory', 'detail', 'desc', 'image']


admin.site.register(Category, CategoryAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)