# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_tenant', '0004_auto_20150208_0210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='product',
            new_name='rental',
        ),
        migrations.AddField(
            model_name='rental',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
