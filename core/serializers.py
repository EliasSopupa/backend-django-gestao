from rest_framework import serializers
from .models import Cliente, Servico, Projeto, Equipa


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'


class EquipaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipa
        fields = '__all__'


class ProjetoSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(
        source='cliente.nome',
        read_only=True
    )

    servicos = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Servico.objects.all()
    )

    equipas = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Equipa.objects.all()
    )

    class Meta:
        model = Projeto
        fields = '__all__'
