from django.contrib import admin
from .models import DadosEntrada, DadosTokenizados
# Register your models here.

@admin.register(DadosEntrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('dados', 'tipo_entrada', 'anexo_arquivo')

@admin.register(DadosTokenizados)
class TokenizadoAdmin(admin.ModelAdmin):
    list_display = ('dados_entrada', 'conteudo_tokenizado', 'tokenizado','timestamp', 'tipo_dado_sensivel')