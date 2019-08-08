from django.db import models


# Create your models here.
class OrderInfo(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    user = models.ForeignKey('df_user.UserInfo')
    date = models.DateTimeField(auto_now=True)
    isPay = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    address = models.CharField(max_length=150)


class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('df_goods.GoodsInfo')
    order = models.ForeignKey(OrderInfo)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField()