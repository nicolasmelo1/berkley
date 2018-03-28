# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .forms import PipelineComercial
from django.shortcuts import render
from .models import Regional,Filial,Comercial,Protocolos,TipodeSeguro,Produto,Expectativa,Status,MotivoPerda
from django.http import HttpResponseRedirect

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
                    'historico_1': form['historico_1'].value(),
                    'historico_2': form['historico_2'].value(),
                    'historico_3': form['historico_3'].value(),
                    'historico_4': form['historico_4'].value(),
                    'historico_5': form['historico_5'].value(),
                    'historico_6': form['historico_6'].value(),
                    'historico_7': form['historico_7'].value(),
                    'historico_8': form['historico_8'].value(),
                    'historico_9': form['historico_9'].value(),
                    'historico_10': form['historico_10'].value()
                })
                return render(request, 'home/home_base.html', {'form': form})
    else:
        form = PipelineComercial()
        return render(request, 'home/home_base.html', {'form': form})
# Create your views here.
