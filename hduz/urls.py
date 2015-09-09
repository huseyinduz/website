from django.conf.urls import patterns, include, url
from django.contrib import admin
from hduz.views import anasayfa
import webcore.urls


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'hduz.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', anasayfa),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'webcore/', include(webcore.urls)),
                       #(r'^ckeditor/', include('ckeditor.urls')),
                       (r'^ckeditor/', include('ckeditor_uploader.urls')),
                       )
