from django.db import models
from tinymce.models import HTMLField


class Category(models.Model):
    title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.title.encode('utf-8')


class GoodsInfo(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='df_goods')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    isDelete = models.BooleanField(default=False)
    unit = models.CharField(max_length=20)
    click = models.IntegerField()
    desc = models.CharField(max_length=500)
    inventory = models.IntegerField()
    detail = HTMLField()
    category = models.ForeignKey(Category)
