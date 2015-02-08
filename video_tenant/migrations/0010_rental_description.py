# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_tenant', '0009_auto_20150208_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
