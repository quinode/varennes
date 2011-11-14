# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

def home(request):
    rdict = {}
    return render_to_response('index.html',rdict,RequestContext(request))