# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.



class baslik(models.Model):
    isim = models.CharField(max_length=50, verbose_name="Konu Başlığı")
    def __unicode__(self):
        return self.isim


class icerik(models.Model):
    bas = models.ForeignKey(baslik)
    altbaslik = models.CharField(max_length=50, verbose_name="Alt Başlık")
    tarih = models.DateTimeField(auto_now_add=True)
    icerisi = RichTextField()
    aktiflik = models.BooleanField(default=True, verbose_name="Aktif Mi ?")

    def __unicode__(self):
        return self.altbaslik

