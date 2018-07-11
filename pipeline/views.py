# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .forms import PipelineComercial, HistoryFormset, Historico
from django.shortcuts import render
from .models import Regionals, Commercials, Subsidiaries, Products, InsuranceType, Expectations, Status, ReasonsForLoss, Congeners
from protocolos.models import Protocols
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta

def temp(request):
    if request.method == 'POST':
        form = PipelineComercial(request.POST)
        formset = HistoryFormset(request.POST)

        if request.POST.get('salvar'):
            print(formset.errors)
            print(form.errors)
            if form.is_valid() and formset.is_valid():
                protocol = form.save(commit=False)
                protocol.regional = form.cleaned_data['regional']
                protocol.subsidiary = form.cleaned_data['subsidiary']
                protocol.commercial = form.cleaned_data['commercial']
                protocol.broker = form['broker'].value()
                protocol.product = form.cleaned_data['product']
                protocol.client = form['client'].value()
                protocol.prize = form['prize'].value()
                protocol.receipt = form.cleaned_data['receipt']
                protocol.maturity = form.cleaned_data['maturity']
                protocol.closure = form.cleaned_data['closure']
                protocol.insurance_type = form.cleaned_data['insurance_type']
                protocol.expectation = form.cleaned_data['expectation']
                protocol.status = form.cleaned_data['status']
                protocol.subscriber = form['subscriber'].value()
                protocol = form.save()
                for index, history_form in enumerate(formset):
                    history = history_form.save(commit=False)
                    history.protocol = protocol
                    history.save()
                return render(request, 'home/home_base.html', {'form': form, 'formset': formset})
    else:
        form = PipelineComercial(request.POST or None)
        formset = HistoryFormset
        return render(request, 'home/home_base.html', {'form': form, 'formset': formset})
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
