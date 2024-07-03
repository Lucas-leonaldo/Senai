from django.urls import path, include
from .views import dashboard_view, processar_dados_entrada
from rest_framework.routers import DefaultRouter
from .views import DadosEntradaViewSet

router = DefaultRouter()
router.register(r'dados_entrada', DadosEntradaViewSet)

urlpatterns = [
    path('entrada/', processar_dados_entrada, name='dados_entrada_form'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('api/', include(router.urls)),
]