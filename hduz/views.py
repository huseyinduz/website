from django.shortcuts import render_to_response
from django.template import RequestContext




def anasayfa(request):

    return render_to_response('anasayfa.html', locals(), context_instance=RequestContext(request))
