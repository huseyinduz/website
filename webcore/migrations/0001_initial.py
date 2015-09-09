# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='baslik',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isim', models.CharField(max_length=50, verbose_name=b'Konu Ba\xc5\x9fl\xc4\xb1\xc4\x9f\xc4\xb1')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='icerik',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('altbaslik', models.CharField(max_length=50, verbose_name=b'Alt Ba\xc5\x9fl\xc4\xb1k')),
                ('link', models.SlugField()),
                ('tarih', models.DateTimeField(auto_now_add=True)),
                ('icerisi', models.TextField(verbose_name=b'\xc4\xb0\xc3\xa7erik')),
                ('aktiflik', models.BooleanField(default=True, verbose_name=b'Aktif Mi ?')),
                ('bas', models.ForeignKey(to='webcore.baslik')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
