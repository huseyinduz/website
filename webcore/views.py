from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext
from .models import *


def linuxicerik(request, altbaslik):
    icerikler = icerik.objects.get(altbaslik=altbaslik)
    return render_to_response("linuxicerik.html", locals(), content_type=RequestContext(request))


def djangoicerik(request, altbaslik):
    djangofiltre = icerik.objects.get(altbaslik=altbaslik)
    return render_to_response("djangomenu.html", locals(), context_instance=RequestContext(request))


def iviriviricerik(request, altbaslik):
    ivirzivirfiltre = icerik.objects.get(altbaslik=altbaslik)
    return render_to_response("ivirzivir.html", locals(), context_instance=RequestContext(request))