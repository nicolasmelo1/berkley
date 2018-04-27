from django.shortcuts import render
from home.models import Protocolos
from home.forms import PipelineComercial


def protocolos(request):
    protocolos = Protocolos.objects.all()
    return render(request, 'protocolos/protocolos_base.html', {'protocolos': protocolos})


