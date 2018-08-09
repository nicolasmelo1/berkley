from django.shortcuts import render
from .models import Protocols
from django.http import HttpResponseRedirect


def protocolos(request, company):
    protocolos = Protocols.objects.all()
    return render(request, 'protocolos/protocolos_base.html', {'protocolos': protocolos, 'company_name': company})


def delete(request, company):
    Protocols.objects.filter(pk=request.POST['delete']).delete()
    return HttpResponseRedirect("/{}/protocolos/".format(company))
