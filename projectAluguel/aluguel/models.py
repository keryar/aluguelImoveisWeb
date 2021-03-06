import datetime

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'


    def __str__(self):
        return self.nome

    def get_absolute_path(self):
        return reverse('aluguel:lista_imoveis_por_categoria', args=[self.slug])


class Imovel(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='imoveis')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    imagem = models.ImageField(upload_to='aluguel/images/apts', blank=False)
    descricao = models.TextField(blank=True)
    dono = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    numero = models.PositiveIntegerField()
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200, db_index=True)
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    cep = models.CharField(max_length=200)
    disponivel = models.BooleanField(default=True)
    data_cadastramento = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    endereco = models.TextField(blank=True)

    class Meta:
        ordering = ('cidade',)
        verbose_name = 'imovel'
        verbose_name_plural = 'imoveis'


    def cadastrado_recentemente(self):
        return self.data_cadastramento >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_path(self):
        return reverse('aluguel:exibe_imovel', args=[self.id, self.slug])

    def __str__(self):
        return self.endereco