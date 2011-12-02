# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from coop_agenda.models import Occurrence,Event,EventType

from datetime import datetime

def home(request):
    rdict = {}
    for evt in EventType.objects.all():
        rdict[evt.abbr] = Occurrence.objects.filter(start_time__gt=datetime.now(),event__event_type=evt)
    return render_to_response('index.html',rdict,RequestContext(request))