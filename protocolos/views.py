from django.shortcuts import render
from home.models import Protocolos


def protocolos(request):
    protocolos = Protocolos.objects.all()
    return render(request, 'protocolos/protocolos_base.html', {'protocolos': protocolos})
