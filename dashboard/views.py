from django.shortcuts import render
from protocolos.models import Protocols
from pipeline.forms import PipelineComercial
from django.http import HttpResponseRedirect


def dashboard(request, company):

    return render(request, 'dashboard/dashboard_base.html', {'dashboard': dashboard, 'company_name': company})
