from django.shortcuts import render
from home.models import Protocolos
from home.forms import PipelineComercial
from django.http import HttpResponseRedirect, JsonResponse
from django.forms.models import model_to_dict
import json

def protocolos(request):
    protocolos = Protocolos.objects.all()
    print(protocolos)
    return render(request, 'protocolos/protocolos_base.html', {'protocolos': protocolos})

def delete(request):
    Protocolos.objects.filter(pk=request.POST['delete']).delete()
    return HttpResponseRedirect("/protocolos/")
