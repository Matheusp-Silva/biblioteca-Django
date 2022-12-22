from django.db import models


class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank=True, null=True)
    data_cadastro = models.DateTimeField()
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=30, blank=True)
    data_emprestado = models.DateTimeField(blank=True, null=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    tempo_duracao = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Livro'