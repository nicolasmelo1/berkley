from django import forms
from .models import Regionals, Commercials, Subsidiaries, Products, InsuranceType, Expectations, Status, ReasonsForLoss, Congeners
from protocolos.models import Protocols

class PipelineComercial(forms.ModelForm):
    error_css_class='error'

    regional = forms.ModelChoiceField(queryset=Regionals.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'regional',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    filial = forms.ModelChoiceField(queryset=Subsidiaries.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'filial',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    comercial = forms.ModelChoiceField(queryset=Commercials.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'comercial',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    corretor = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'corretor',
            'placeholder': 'Escreva aqui o nome do corretor',
            'type': 'text',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    premio = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'premio',
            'placeholder': 'Insira o valor mensal da conta',
            'type': 'number',
            'style': '-webkit-appearance: none;-moz-appearance: textfield; background-color: #f2f2f2; border:1px solid #444444',

        }
    ))
    produto = forms.ModelChoiceField(queryset=Products.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'placeholder': 'Esolha o produto',
            'id': 'produto',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    cliente = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'cliente',
            'placeholder': 'Escreva aqui o nome da empresa cliente',
            'type': 'text',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    subscritor = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'subscritor',
            'type': 'text',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    recebimento = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'recebimento',
            'type': 'text',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    fechamento = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'fechamento',
            'placeholder': 'Data prevista para fechamento',
            'type': 'text',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    vencimento = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'vencimento',
            'placeholder': 'Data de vencimento da apólice',
            'type': 'text',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    tipo_de_seguro = forms.ModelChoiceField(queryset=InsuranceType.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'tipo_de_seguro',
            'style': 'background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    congenere = forms.ModelChoiceField(required=False, queryset=Congeners.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'congenere',
            'style': 'background-color: #f2f2f2; border:1px solid #0dbf7e'
        }
    ))
    expectativa = forms.ModelChoiceField(queryset=Expectations.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'expectativa',
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
    motivo_perda = forms.ModelChoiceField(required=False, queryset=ReasonsForLoss.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'motivo_perda',
            'style': 'background-color: #f2f2f2; border:1px solid #0dbf7e'
        }
    ))
    comentario_perda = forms.CharField(required=False,max_length=200, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'comentario_perda',
            'rows': '1',
            'placeholder': 'Comente brevemente o motivo da perda',
            'style': 'resize: none; background-color: #f2f2f2; border:1px solid #0dbf7e'
        }
    ))
    historico_1 = forms.CharField(required=False, max_length=3000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'historico_1',
            'rows': '2',
            'placeholder': 'Historico 1',
            'style': 'resize: none; background-color: #f2f2f2; border:1px solid #444444'
        }
    ))
    class Meta:
        model = Protocols
        exclude = ('comentario_perda', 'motivo_perda', 'congenere')