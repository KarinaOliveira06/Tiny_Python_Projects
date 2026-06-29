from django import forms
from .models import Cliente, Conta

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'email']

class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ['cliente', 'numero_conta']

class OperacaoForm(forms.Form):
    valor = forms.DecimalField(max_digits=12, decimal_places=2, min_value=0.01)