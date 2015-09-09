from django import template
from django.utils.safestring import mark_safe
from webcore.models import icerik

register = template.Library()


@register.simple_tag
def linuxmenu():
    filtre = icerik.objects.filter(bas_id=1)
    html = ""
    for i in filtre:
        html += """<li><a href="#" onclick="icerikgetir('/webcore/linuxicerik/%s','lxicerik')" data-toggle="modal"
           data-target="#linuxdersler">%s</a></li>""" % (i.altbaslik, i.altbaslik)
    
    return mark_safe(html)


@register.simple_tag()
def djangomenu():
    djfiltre = icerik.objects.filter(bas_id=2)
    html = ""
    for i in djfiltre:
        html += """<li><a href="#" onclick="icerikgetir('/webcore/djangoicerik/%s','djicerik')" data-toggle="modal"
           data-target="#djangodersler">%s</a></li>""" % (i.altbaslik, i.altbaslik)

    return mark_safe(html)

@register.simple_tag()
def ivirzivirmenu():
    ivirfiltre = icerik.objects.filter(bas_id=3)
    html = ""
    for i in ivirfiltre:
        html += """<li><a href="#" onclick="icerikgetir('/webcore/ivirziviricerik/%s','iicerik')" data-toggle="modal"
           data-target="#ivirzivirdersler">%s</a></li>""" % (i.altbaslik, i.altbaslik)

    return mark_safe(html)

