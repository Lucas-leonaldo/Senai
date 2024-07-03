from django.db import models
from .models import DadosTokenizados
import matplotlib.pyplot as plt
import io
import base64

def obter_estatisticas_dados_sensiveis():
    total_tokenizado = DadosTokenizados.objects.count()
    tipos_dados = DadosTokenizados.objects.values('tipo_dado_sensivel').annotate(count=models.Count('id'))
    return total_tokenizado, tipos_dados

def gerar_grafico_dados():
    _, tipos_dados = obter_estatisticas_dados_sensiveis()
    labels = [dados['tipo_dado_sensivel'] for dados in tipos_dados]
    counts = [dados['count'] for dados in tipos_dados]
    
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode('utf-8')