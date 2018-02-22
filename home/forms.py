from django import forms
from .models import Regional, Filial, Comercial, Produto, MotivoPerda,TipodeSeguro, Status, Expectativa, Protocolos

class PipelineComercial(forms.ModelForm):
    error_css_class='error'

    protocolo = forms.CharField(max_length=20, widget=forms.TextInput)
    regional = forms.ModelChoiceField(queryset=Regional.objects.all())
    filial = forms.ModelChoiceField(queryset=Filial.objects.all())
    comercial = forms.ModelChoiceField(queryset=Comercial.objects.all())
    corretor = forms.CharField(max_length=200, widget=forms.TextInput)
    produto = forms.ModelChoiceField(queryset=Produto.objects.all())
    cliente = forms.CharField(max_length=200, widget=forms.TextInput)
    recebimento = forms.DateField(widget=forms.SelectDateWidget)
    fechamento = forms.DateField(widget=forms.SelectDateWidget)
    vencimento = forms.DateField(widget=forms.SelectDateWidget)
    tipo_de_seguro = forms.ModelChoiceField(queryset=TipodeSeguro.objects.all())
    expectatva = forms.ModelChoiceField(queryset=Expectativa.objects.all())
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    subscritor = forms.CharField(max_length=200, widget=forms.TextInput)
    motivo_perda = forms.ModelChoiceField(queryset=MotivoPerda.objects.all())

    class Meta:
        model=Protocolos
        fields = '__all__'