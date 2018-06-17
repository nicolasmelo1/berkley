from django.shortcuts import render
from home.models import Protocolos
from home.forms import PipelineComercial
from django.http import HttpResponseRedirect


def dashboard(request):

    return render(request, 'dashboard/dashboard_base.html', {'dashboard': dashboard})
