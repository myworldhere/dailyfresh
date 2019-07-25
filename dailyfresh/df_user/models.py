# coding=utf-8
from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=40)
    email = models.CharField(max_length=30)
    consignee = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=100, default='')
    postcode = models.CharField(max_length=6, default='')
    phone = models.CharField(max_length=11, default='')
    # default, blank 是python层面的约束，不影响数据库表结构，因此不需要迁移