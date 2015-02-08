# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_tenant', '0003_auto_20150208_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'media/product_pictures', blank=True)),
                ('description', models.CharField(max_length=140, null=True, blank=True)),
                ('product', models.ForeignKey(related_name='pictures', to='video_tenant.Rental')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rental',
            name='pricing',
            field=models.DecimalField(default=10.00, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]
