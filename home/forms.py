from django import forms
from .models import Regional, Filial, Comercial, Produto, MotivoPerda,TipodeSeguro, Status, Expectativa, Protocolos

class PipelineComercial(forms.ModelForm):
    error_css_class='error'

    regional = forms.ModelChoiceField(queryset=Regional.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'regional'
        }
    ))
    filial = forms.ModelChoiceField(queryset=Filial.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'filial'
        }
    ))
    comercial = forms.ModelChoiceField(queryset=Comercial.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'comercial'
        }
    ))
    corretor = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'corretor',
            'placeholder': 'Escreva aqui o nome do corretor',
            'type': 'text'
        }
    ))
    premio = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'premio',
            'placeholder': 'Insira o valor mensal da conta',
            'type': 'number',
            'style': '-webkit-appearance: none;-moz-appearance: textfield;'
        }
    ))
    produto = forms.ModelChoiceField(queryset=Produto.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'placeholder': 'Esolha o produto',
            'id': 'produto'
        }
    ))
    cliente = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'cliente',
            'placeholder': 'Escreva aqui o nome da empresa cliente',
            'type': 'text'
        }
    ))
    subscritor = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'subscritor',
            'type': 'text'
        }
    ))
    recebimento = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'recebimento',
            'type': 'text'
        }
    ))
    fechamento = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'fechamento',
            'placeholder': 'Data prevista para fechamento',
            'type': 'text'
        }
    ))
    vencimento = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'vencimento',
            'placeholder': 'Data de vencimento da apólice',
            'type': 'text'
        }
    ))
    tipo_de_seguro = forms.ModelChoiceField(queryset=TipodeSeguro.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'tipo_de_seguro'
        }
    ))
    congenere = forms.ModelChoiceField(required=False, queryset=TipodeSeguro.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'congenere'
        }
    ))
    expectativa = forms.ModelChoiceField(queryset=Expectativa.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'expectativa'
        }
    ))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'status'
        }
    ))
    motivo_perda = forms.ModelChoiceField(required=False, queryset=MotivoPerda.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'motivo_perda'
        }
    ))
    historico_1 = forms.CharField(required=False,max_length=3000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'historico_1',
            'rows': '2',
            'placeholder': 'Historico 1',
            'style': 'resize: none'
        }
    ))
    historico_2 = forms.CharField(required=False,max_length=3000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'historico_2',
            'rows': '2',
            'placeholder': 'Historico 2',
            'style': 'resize: none'
        }
    ))
    historico_3 = forms.CharField(required=False,max_length=3000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'historico_3',
            'rows': '2',
            'placeholder': 'Historico 3',
            'style': 'resize: none'
        }
    ))
    historico_4 = forms.CharField(required=False,max_length=3000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'historico_4',
            'rows': '2',
            'placeholder': 'Historico 4',
            'style': 'resize: none'
        }
    ))
    historico_5 = forms.CharField(required=False,max_length=3000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'historico_5',
            'rows': '2',
            'placeholder': 'Historico 5',
            'style': 'resize: none'
        }
    ))
    historico_6 = forms.CharField(required=False,max_length=3000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'historico_6',
            'rows': '2',
            'placeholder': 'Historico 6',
            'style': 'resize: none'
        }
    ))
    historico_7 = forms.CharField(required=False,max_length=3000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'historico_7',
            'rows': '2',
            'placeholder': 'Historico 7',
            'style': 'resize: none'
        }
    ))
    historico_8 = forms.CharField(required=False,max_length=3000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'historico_8',
            'rows': '2',
            'placeholder': 'Historico 8',
            'style': 'resize: none'
        }
    ))
    historico_9 = forms.CharField(required=False,max_length=3000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'historico_9',
            'rows': '2',
            'placeholder': 'Historico 9',
            'style': 'resize: none'
        }
    ))
    historico_10 = forms.CharField(required=False,max_length=3000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'historico_10',
            'rows': '2',
            'placeholder': 'Historico 10',
            'style': 'resize: none'
        }
    ))
    class Meta:
        model = Protocolos
        exclude = ('comentario_perda', 'motivo_perda', 'congenere')