from django.db import models

# Create your models here.

class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=128)
    motor_jogos = models.CharField(max_length=128)
    ano_fundada = models.DateField()

    def __str__(self):
        return self.nome

class Plataforma(models.Model):
    tipo = models.CharField(max_length=32)
    nome = models.CharField(max_length=128)
    ano_lancamento = models.DateField(blank=True, null=True)
    geracao = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    titulo = models.CharField(max_length=128)
    descricao = models.TextField()
    genero = models.CharField(max_length=128)
    lancamento = models.DateField()

    desenvolvedor = models.ForeignKey(Desenvolvedor, on_delete=models.SET_NULL, null=True)

    plataforma = models.ManyToManyField(Plataforma)

    def __str__(self):
        return self.titulo