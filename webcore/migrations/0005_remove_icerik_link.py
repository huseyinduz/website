# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0004_auto_20150608_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icerik',
            name='link',
        ),
    ]
