from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    localizacao = models.CharField(max_length=100)


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo = models.CharField(max_length=50)
    preco_base = models.DecimalField(max_digits=10, decimal_places=2)


class Equipa(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=100)
    contacto = models.CharField(max_length=20)


class Projeto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(Servico)
    equipas = models.ManyToManyField(Equipa)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=50)
    local_execucao = models.CharField(max_length=100)

    def __str__(self):
        return f"Projeto #{self.id}"



