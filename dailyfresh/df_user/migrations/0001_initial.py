# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=30)),
                ('consignee', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
    ]
