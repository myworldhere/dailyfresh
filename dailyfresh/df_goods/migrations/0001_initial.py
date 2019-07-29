# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to=b'df_goods')),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('isDelete', models.BooleanField(default=False)),
                ('unit', models.CharField(max_length=20)),
                ('click', models.IntegerField()),
                ('desc', models.CharField(max_length=500)),
                ('inventory', models.IntegerField()),
                ('detail', tinymce.models.HTMLField()),
                ('category', models.ForeignKey(to='df_goods.Category')),
            ],
        ),
    ]
