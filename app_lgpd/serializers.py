from rest_framework import serializers
from .models import DadosEntrada

class DadosEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosEntrada
        fields = ['dados', 'tipo_entrada', 'anexo_arquivo']