# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .forms import PipelineComercial, HistoryFormset, ClientsForm, PersonsFormset
from django.shortcuts import render, redirect
from protocolos.models import Protocols, History
from login.models import Companies
from berkley.defaults import PermissionHandler
from datetime import datetime
from django.views import View
from django.contrib.auth.decorators import login_required


class Form(View):
    template_name = 'pipeline/pipeline_base.html'
    pipeline_history_formset = HistoryFormset()
    business_plan_formset = PersonsFormset()
    business_plan_form = ClientsForm()

    def get_pipeline(self, user, company):
        companies = Companies.objects.get(endpoint=company)
        pipeline_form = PipelineComercial(user=user, company=companies)
        return pipeline_form


class Pipeline(Form):
    def get(self, request, company, *args, **kwargs):
        user = request.user
        pipeline_form = self.get_pipeline(user, company)
        return render(request, self.template_name,
                      {
                          'form': pipeline_form,
                          'formset': self.pipeline_history_formset,
                          'business_plan_form': self.business_plan_form,
                          'business_plan_formset': self.business_plan_formset,
                          'company_name': company
                      })

    def post(self, request, company, *args, **kwargs):
        user = request.user
        pipeline_form = self.get_pipeline(user, company)
        if request.POST.get('salvar'):
            if pipeline_form.is_valid() and self.pipeline_history_formset.is_valid():
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
                for history_form in reversed(self.pipeline_history_formset):
                    history = history_form.save(commit=False)
                    history.protocol = protocol
                    history.save()
                return render(request, self.template_name,
                              {
                                  'form': pipeline_form,
                                  'formset': self.pipeline_history_formset,
                                  'business_plan_form': self.business_plan_form,
                                  'business_plan_formset': self.business_plan_formset,
                                  'render_business_plan_first': False,
                                  'company_name': company
                              })


class PipelineEdit(Form):
    def get(self, request, pk, company):
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

        return render(request,  self.template_name, {
            'pipeline_form': pipeline_form,
            'pipeline_formset': pipeline_history_formset,
            'company_name': company
        })


class BusinessPlan(Form):
    def post(self, request, company):
        user = request.user
        if self.business_plan_form.is_valid() and self.business_plan_formset.is_valid():
            business_plan_save = self.business_plan_form.save(commit=False)
            business_plan_save.name = self.business_plan_form['name'].value()
            business_plan_save.revenues = self.business_plan_form['revenues'].value()
            business_plan_save.foundation_date = self.business_plan_form.cleaned_data['foundation_date']
            business_plan_save.employees = self.business_plan_form['employees'].value()
            business_plan_save.address = self.business_plan_form['address'].value()
            business_plan_save.user = user
            business_plan_save = self.business_plan_form.save()
            for persons_form in reversed(self.business_plan_formset):
                persons_save = persons_form.save(commit=False)
                persons_save.client = business_plan_save
                persons_save.name = persons_form['name'].value()
                persons_save.email = persons_form['email'].value()
                persons_save.cellphone_number = persons_form['cellphone_number'].value()
                persons_save.birthday = datetime.strptime(persons_form['birthday'].value(), '%d/%m/%Y')
                persons_save.occupation = persons_form['occupation'].value()
                persons_save.hobby = persons_form['hobby'].value()
                persons_save.save()
            return redirect('pipeline', company)
