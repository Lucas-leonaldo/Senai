# meuapp/models.py
from django.db import models

class DadosEntrada(models.Model):
    MANUAL = 'MAN'
    AUTOMATICO = 'AUTO'
    TIPOS_ENTRADA = [
        (MANUAL, 'Manual'),
        (AUTOMATICO, 'Automático'),
    ]
    
    dados = models.TextField()
    tipo_entrada = models.CharField(max_length=4, choices=TIPOS_ENTRADA, default=AUTOMATICO)
    anexo_arquivo = models.FileField(upload_to='anexos/', null=True, blank=True)

class DadosTokenizados(models.Model):
    dados_entrada = models.ForeignKey(DadosEntrada, on_delete=models.DO_NOTHING)
    conteudo_tokenizado = models.TextField()
    tokenizado = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    tipo_dado_sensivel = models.CharField(max_length=100, null=True, blank=True)