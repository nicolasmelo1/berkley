from django import forms
from django.forms import formset_factory
from .models import Regionals, Commercials, Subsidiaries, Products, InsuranceType, Expectations, Status, ReasonsForLoss, Congeners
from protocolos.models import Protocols, History


class PipelineComercial(forms.ModelForm):
    error_css_class='error'

    regional = forms.ModelChoiceField(queryset=Regionals.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'regional',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    subsidiary = forms.ModelChoiceField(queryset=Subsidiaries.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'subsidiary',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    commercial = forms.ModelChoiceField(queryset=Commercials.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'commercial',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    broker = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'broker',
            'placeholder': 'Escreva aqui o nome do corretor',
            'type': 'text',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    prize = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'prize',
            'placeholder': 'Insira o valor mensal da conta',
            'type': 'number',
            'style': '-webkit-appearance: none;-moz-appearance: textfield; background-color: #f2f2f2; border:1px solid #444444',

        }
    ))
    product = forms.ModelChoiceField(queryset=Products.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'placeholder': 'Esolha o produto',
            'id': 'product',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    client = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'client',
            'placeholder': 'Escreva aqui o nome da empresa cliente',
            'type': 'text',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    subscriber = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'subscriber',
            'type': 'text',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    receipt = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'receipt',
            'type': 'text',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    closure = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'closure',
            'placeholder': 'Data prevista para fechamento',
            'type': 'text',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    maturity = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'maturity',
            'placeholder': 'Data de vencimento da apólice',
            'type': 'text',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    insurance_type = forms.ModelChoiceField(queryset=InsuranceType.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'insurance_type',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    congener = forms.ModelChoiceField(required=False, queryset=Congeners.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'congener',
            'style': 'background-color: #f2f2f2; border:1px solid #0dbf7e'
        }
    ))
    expectation = forms.ModelChoiceField(queryset=Expectations.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'expectation',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'status',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    reason_for_loss = forms.ModelChoiceField(required=False, queryset=ReasonsForLoss.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'loss_detail',
            'style': 'background-color: #f2f2f2; border:1px solid #0dbf7e'
        }
    ))
    loss_comment = forms.CharField(required=False,max_length=200, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'comentario_perda',
            'rows': '1',
            'placeholder': 'Comente brevemente o motivo da perda',
            'style': 'resize: none; background-color: #f2f2f2; border:1px solid #0dbf7e'
        }
    ))


    class Meta:
        model = Protocols
        exclude = ('loss_comment', 'loss_detail', 'congener', 'reason_for_loss')


class Historico(forms.ModelForm):
    history = forms.CharField(required=False, max_length=3000, widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '2',
                'placeholder': 'Historico #1',
                'style': 'resize: none; background-color: #f2f2f2; border:1px solid #444444;'
            }
        ))

    class Meta:
        model = History
        exclude = ('protocol',)


HistoryFormset = formset_factory(Historico, extra=0, min_num=1, can_order=True)
