# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_tenant', '0006_rental_default_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='city',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rental',
            name='number',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rental',
            name='state',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rental',
            name='street',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rental',
            name='zipcode',
            field=models.CharField(max_length=5, blank=True),
            preserve_default=True,
        ),
    ]
