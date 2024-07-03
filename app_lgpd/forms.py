# meuapp/forms.py
from django import forms
from .models import DadosEntrada

class DadosEntradaForm(forms.ModelForm):
    class Meta:
        model = DadosEntrada
        fields = ['dados', 'tipo_entrada', 'anexo_arquivo']
