# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .forms import PipelineComercial, HistoryFormset, Historico
from django.shortcuts import render
from protocolos.models import Protocols, History
from login.models import Companies
from berkley.defaults import PermissionHandler


def temp(request, company):
    user = request.user
    companies = Companies.objects.get(endpoint=company)

    if request.method == 'POST':
        form = PipelineComercial(request.POST, user=user, company=companies)
        formset = HistoryFormset(request.POST)
        if request.POST.get('salvar'):
            print(form.errors)
            print(formset.errors)
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
                for history_form in reversed(formset):
                    history = history_form.save(commit=False)
                    history.protocol = protocol
                    history.save()
                return render(request, 'pipeline/pipeline_base.html', {'form': form,
                                                                       'formset': formset,
                                                                       'company_name': company})
    else:
        form = PipelineComercial(request.POST or None, user=user, company=companies)
        formset = HistoryFormset
        return render(request, 'pipeline/pipeline_base.html', {'form': form, 'formset': formset, 'company_name': company})


def consulta(request, pk):
    user = request.user
    protocolo = Protocols.objects.get(pk=pk)
    historicos = History.objects.filter(protocol=pk)

    form = PipelineComercial(user=user, initial={
        'regional': protocolo.regional,
        'subsidiary': protocolo.subsidiary,
        'commercial': protocolo.commercial,
        'broker': protocolo.broker,
        'client': protocolo.client,
        'product': protocolo.product,
        'receipt': protocolo.receipt.strftime('%d/%m/%Y'),
        'closure': protocolo.closure.strftime('%d/%m/%Y'),
        'maturity': protocolo.maturity.strftime('%d/%m/%Y'),
        'prize': protocolo.prize,
        'insurance_type': protocolo.insurance_type,
        'expectation': protocolo.expectation,
        'status': protocolo.status,
        'subscriber': protocolo.subscriber,
        })

    formset = HistoryFormset(initial=[{
        'history': historico.history
    } for historico in reversed(historicos)])

    return render(request, 'pipeline/pipeline_base.html', {
        'form': form,
        'formset': formset,
        'type': 'consulta'
    })
