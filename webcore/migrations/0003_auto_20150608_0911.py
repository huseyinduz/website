# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0002_auto_20150606_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icerik',
            name='icerisi',
            field=models.TextField(verbose_name=b'icerik'),
            preserve_default=True,
        ),
    ]
