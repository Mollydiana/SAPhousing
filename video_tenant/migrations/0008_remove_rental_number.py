# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_tenant', '0007_auto_20150208_0816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='number',
        ),
    ]
