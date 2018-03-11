from django import forms
from .models import Regional, Filial, Comercial, Produto, MotivoPerda,TipodeSeguro, Status, Expectativa, Protocolos

class PipelineComercial(forms.ModelForm):
    error_css_class='error'

    protocolo = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'protocolo',
            'type': 'text',
            'placeholder': 'Protocolo para editar'
        }
    ))
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
            'type': 'text'
        }
    ))
    produto = forms.ModelChoiceField(queryset=Produto.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'produto'
        }
    ))
    cliente = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'cliente',
            'type': 'text'
        }
    ))
    recebimento = forms.DateField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'recebimento',
            'type': 'text'
        }
    ))
    fechamento = forms.DateField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'fechamento',
            'type': 'text'
        }
    ))
    vencimento = forms.DateField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'vencimento',
            'type': 'text'
        }
    ))
    tipo_de_seguro = forms.ModelChoiceField(queryset=TipodeSeguro.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'tipo_de_seguro'
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
    subscritor = forms.CharField(max_length=200, widget=forms.TextInput)
    motivo_perda = forms.ModelChoiceField(queryset=MotivoPerda.objects.all())

    class Meta:
        model=Protocolos
        fields = '__all__'