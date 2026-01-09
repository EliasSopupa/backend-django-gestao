from django.shortcuts import render
from rest_framework import viewsets, serializers
from .models import Cliente, Servico, Projeto, Equipa
from .serializers import (
    ClienteSerializer,
    ServicoSerializer,
    ProjetoSerializer,
    EquipaSerializer
)

class ClienteViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para Clientes da SOPUKA
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para Serviços oferecidos pela SOPUKA
    """
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class EquipaViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para Equipas Técnicas
    """
    queryset = Equipa.objects.all()
    serializer_class = EquipaSerializer

class ProjetoViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para Projetos da SOPUKA
    """
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer



