# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .forms import PipelineComercial
from django.shortcuts import render
from django.http import HttpResponseRedirect

def temp(request):
    return render(request, 'home/home_base.html', {'form': PipelineComercial()})
# Create your views here.
