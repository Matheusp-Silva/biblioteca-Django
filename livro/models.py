from django.db import models
from django.utils.timezone import now

class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank=True, null=True)
    data_cadastro = models.DateTimeField(default=now())
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=30, blank=True, null=True)
    data_emprestado = models.DateTimeField(blank=True, null=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    tempo_duracao = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome