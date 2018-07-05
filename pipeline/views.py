# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .forms import PipelineComercial
from django.shortcuts import render
from .models import Regionals, Commercials, Subsidiaries, Products, InsuranceType, Expectations, Status, ReasonsForLoss, Congeners
from protocolos.models import Protocols
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta

def temp(request):
    if request.method == 'POST':
        form = PipelineComercial(request.POST)
        if request.POST.get('salvar'):
            print(form.errors)
            if form.is_valid():
                save = form.save(commit=False)
                save.regional = form.cleaned_data['regional']
                save.filial = form.cleaned_data['filial']
                save.comercial = form.cleaned_data['comercial']
                save.corretor = form['corretor'].value()
                save.produto = form.cleaned_data['produto']
                save.cliente = form['cliente'].value()
                save.premio = form['premio'].value()
                save.recebimento = form.cleaned_data['recebimento']
                save.vencimento = form.cleaned_data['vencimento']
                save.fechamento = form.cleaned_data['fechamento']
                save.tipo_de_seguro = form.cleaned_data['tipo_de_seguro']
                save.expectativa = form.cleaned_data['expectativa']
                save.status = form.cleaned_data['status']
                save.subscritor = form['subscritor'].value()
                save.save()
                form = PipelineComercial(initial={
                    'regional': form.cleaned_data['regional'],
                    'filial': form.cleaned_data['filial'],
                    'comercial': form.cleaned_data['filial'],
                    'corretor': form['corretor'].value(),
                    'cliente': form['cliente'].value(),
                    'produto': form.cleaned_data['produto'],
                    'recebimento': form['recebimento'].value(),
                    'fechamento': form['fechamento'].value(),
                    'vencimento': form['vencimento'].value(),
                    'premio': form['premio'].value(),
                    'tipo_de_seguro': form.cleaned_data['tipo_de_seguro'],
                    'expectativa': form.cleaned_data['expectativa'],
                    'status': form.cleaned_data['status'],
                    'subscritor': form['subscritor'].value(),
                })
                return render(request, 'home/home_base.html', {'form': form})
    else:
        form = PipelineComercial()
        return render(request, 'home/home_base.html', {'form': form})
# Create your views here.


def consulta(request, pk):

    protocolo = Protocols.objects.get(pk=pk)

    form = PipelineComercial(initial={
        'regional': protocolo.regional,
        'filial': protocolo.filial,
        'comercial': protocolo.comercial,
        'corretor': protocolo.corretor,
        'cliente': protocolo.cliente,
        'produto': protocolo.produto,
        'recebimento': protocolo.recebimento.strftime('%d/%m/%Y'),
        'fechamento': protocolo.fechamento.strftime('%d/%m/%Y'),
        'vencimento': protocolo.vencimento.strftime('%d/%m/%Y'),
        'premio': protocolo.premio,
        'tipo_de_seguro': protocolo.tipo_de_seguro,
        'expectativa': protocolo.expectativa,
        'status': protocolo.status,
        'subscritor': protocolo.subscritor,
        })

    return render(request, 'home/home_base.html', {'form': form})
