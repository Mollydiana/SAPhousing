# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_tenant', '0005_auto_20150208_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='default_picture',
            field=models.ForeignKey(related_name='rentals', blank=True, to='video_tenant.Picture', null=True),
            preserve_default=True,
        ),
    ]
