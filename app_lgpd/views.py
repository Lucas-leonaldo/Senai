from django.shortcuts import render, redirect
from .forms import DadosEntradaForm
from .models import DadosEntrada, DadosTokenizados
from rest_framework import viewsets
from .utils import obter_estatisticas_dados_sensiveis, gerar_grafico_dados
from .serializers import DadosEntradaSerializer
import re

def processar_dados_entrada(request):
    if request.method == 'POST':
        form = DadosEntradaForm(request.POST, request.FILES)
        if form.is_valid():
            dados_entrada = form.save()
            if dados_entrada.tipo_entrada == DadosEntrada.MANUAL and dados_entrada.anexo_arquivo:
                pass
            if precisa_tokenizar(dados_entrada.dados):
                conteudo_tokenizado = tokenizar_dados(dados_entrada.dados)
                DadosTokenizados.objects.create(
                    dados_entrada=dados_entrada,
                    conteudo_tokenizado=conteudo_tokenizado,
                    tokenizado=True,
                    tipo_dado_sensivel="CPF"
                )
            return redirect('dashboard')
    else:
        form = DadosEntradaForm()
    return render(request, 'dados_entrada_form.html', {'form': form})

def precisa_tokenizar(dados):
    return bool(re.search(r'\b(?:CPF|RG|CNPJ)\b', dados))

def tokenizar_dados(dados):
    tokenizado = re.sub(r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b', 'TOKEN_CPF', dados)
    tokenizado = re.sub(r'\b\d{2}\.\d{3}\.\d{3}-\d\b', 'TOKEN_RG', tokenizado)
    return tokenizado

class DadosEntradaViewSet(viewsets.ModelViewSet):
    queryset = DadosEntrada.objects.all()
    serializer_class = DadosEntradaSerializer

def dashboard_view(request):
    total_tokenizado, tipos_dados = obter_estatisticas_dados_sensiveis()
    grafico = gerar_grafico_dados()
    context = {
        'total_tokenizado': total_tokenizado,
        'tipos_dados': tipos_dados,
        'grafico': grafico,
    }
    return render(request, 'dashboard.html', context)