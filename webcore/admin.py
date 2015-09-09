from django.contrib import admin
from .models import *

# Register your models here.





class baslikadmin(admin.ModelAdmin):
    class Meta:
        model = baslik


class icerikadmin(admin.ModelAdmin):
    class Meta:
        model = icerik


admin.site.register(baslik, baslikadmin)
admin.site.register(icerik, icerikadmin)


