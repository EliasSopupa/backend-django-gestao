from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClienteViewSet,
    ServicoViewSet,
    ProjetoViewSet,
    EquipaViewSet
)

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'servicos', ServicoViewSet)
router.register(r'projetos', ProjetoViewSet)
router.register(r'equipas', EquipaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
