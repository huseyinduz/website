from django.conf.urls import patterns, url
from webcore.views import linuxicerik, djangoicerik,iviriviricerik

urlpatterns = patterns('',

                       url(r'linuxicerik/(?P<altbaslik>.*)/$', linuxicerik),
                       url(r'djangoicerik/(?P<altbaslik>.*)/$', djangoicerik),
                       url(r'ivirziviricerik/(?P<altbaslik>.*)/$', iviriviricerik),

                       )
