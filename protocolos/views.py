from django.shortcuts import render
from .models import Protocols
from django.http import HttpResponseRedirect

def protocolos(request):
    protocolos = Protocols.objects.all()
    print(protocolos)
    return render(request, 'protocolos/protocolos_base.html', {'protocolos': protocolos})


def delete(request):
    Protocols.objects.filter(pk=request.POST['delete']).delete()
    return HttpResponseRedirect("/protocolos/")
