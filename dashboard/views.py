from django.shortcuts import render
from protocolos.models import Protocols
from pipeline.forms import PipelineComercial
from django.http import HttpResponseRedirect


def dashboard(request):

    return render(request, 'dashboard/dashboard_base.html', {'dashboard': dashboard})
