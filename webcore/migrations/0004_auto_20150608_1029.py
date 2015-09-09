# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0003_auto_20150608_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icerik',
            name='icerisi',
            field=ckeditor.fields.RichTextField(),
            preserve_default=True,
        ),
    ]
