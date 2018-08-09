# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .forms import PipelineComercial, HistoryFormset, ClientsForm, PersonsFormset
from django.shortcuts import render
from protocolos.models import Protocols, History
from login.models import Companies
from berkley.defaults import PermissionHandler
from django.contrib.auth.decorators import login_required


@login_required()
def temp(request, company):
    user = request.user
    companies = Companies.objects.get(endpoint=company)
    if request.method == 'POST':
        pipeline_form = PipelineComercial(request.POST, user=user, company=companies)
        pipeline_history_formset = HistoryFormset(request.POST)
        business_plan_formset = PersonsFormset(request.POST)
        business_plan_form = ClientsForm(request.POST or None)
        if request.POST.get('salvar'):
            if pipeline_form.is_valid() and pipeline_history_formset.is_valid():
                protocol = pipeline_form.save(commit=False)
                protocol.regional = pipeline_form.cleaned_data['regional']
                protocol.subsidiary = pipeline_form.cleaned_data['subsidiary']
                protocol.commercial = pipeline_form.cleaned_data['commercial']
                protocol.broker = pipeline_form['broker'].value()
                protocol.product = pipeline_form.cleaned_data['product']
                protocol.client = pipeline_form['client'].value()
                protocol.prize = pipeline_form['prize'].value()
                protocol.receipt = pipeline_form.cleaned_data['receipt']
                protocol.maturity = pipeline_form.cleaned_data['maturity']
                protocol.closure = pipeline_form.cleaned_data['closure']
                protocol.insurance_type = pipeline_form.cleaned_data['insurance_type']
                protocol.expectation = pipeline_form.cleaned_data['expectation']
                protocol.status = pipeline_form.cleaned_data['status']
                protocol.subscriber = pipeline_form['subscriber'].value()
                protocol = pipeline_form.save()
                for history_form in reversed(pipeline_history_formset):
                    history = history_form.save(commit=False)
                    history.protocol = protocol
                    history.save()
                return render(request, 'pipeline/pipeline_base.html', {'form': pipeline_form,
                                                                       'formset': pipeline_history_formset,
                                                                       'business_plan_form': business_plan_form,
                                                                       'business_plan_formset': business_plan_formset,
                                                                       'company_name': company})
    else:
        form = PipelineComercial(request.POST or None, user=user, company=companies)
        business_plan_form = ClientsForm(request.POST or None)
        formset = HistoryFormset
        business_plan_formset = PersonsFormset
        return render(request, 'pipeline/pipeline_base.html',
                      {
                          'form': form,
                          'formset': formset,
                          'business_plan_form': business_plan_form,
                          'business_plan_formset': business_plan_formset,
                          'company_name': company
                      })


@login_required()
def consulta(request, pk, company):
    user = request.user
    companies = Companies.objects.get(endpoint=company)

    protocolo = Protocols.objects.get(pk=pk)
    historicos = History.objects.filter(protocol=pk)

    pipeline_form = PipelineComercial(user=user, company=companies, initial={
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

    pipeline_history_formset = HistoryFormset(initial=[{
        'history': historico.history
    } for historico in reversed(historicos)])

    return render(request, 'pipeline/pipeline_base.html', {
        'pipeline_form': pipeline_form,
        'pipeline_formset': pipeline_history_formset,
        'company_name': company
    })
