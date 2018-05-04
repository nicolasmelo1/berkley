from django.shortcuts import render
from home.models import Protocolos
from home.forms import PipelineComercial
from django.http import HttpResponseRedirect


def protocolos(request):
    protocolos = Protocolos.objects.all()
    return render(request, 'protocolos/protocolos_base.html', {'protocolos': protocolos})

def delete(request):
    Protocolos.objects.filter(pk=request.POST['delete']).delete()
    return HttpResponseRedirect("/protocolos/")
