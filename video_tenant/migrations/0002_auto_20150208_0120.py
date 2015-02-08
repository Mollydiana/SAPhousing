# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('video_tenant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateField(default=datetime.date(2015, 2, 8)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='people',
            name='user_type',
            field=models.IntegerField(default=0, choices=[(0, b'landlord'), (1, b'tenant')]),
            preserve_default=True,
        ),
    ]
