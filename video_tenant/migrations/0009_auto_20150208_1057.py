# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_tenant', '0008_remove_rental_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.IntegerField(default=1, choices=[(0, b'landlord'), (1, b'tenant')]),
            preserve_default=True,
        ),
    ]
