# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


# Create your models here.
class Regional(models.Model):
    regional = models.CharField(max_length=200)
    def __str__(self):
        return self.regional

class Filial(models.Model):
    filial = models.CharField(max_length=200)
    def __str__(self):
        return self.filial

class Comercial(models.Model):
    comercial = models.CharField(max_length=200)
    def __str__(self):
        return self.comercial

class Produto(models.Model):
    produto = models.CharField(max_length=200)
    def __str__(self):
        return self.produto

class TipodeSeguro(models.Model):
    tipo = models.CharField(max_length=200)
    def __str__(self):
        return self.tipo

class Expectativa(models.Model):
    expectativa = models.CharField(max_length=200)
    def __str__(self):
        return self.expectativa

class Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class MotivoPerda(models.Model):
    motivo = models.CharField(max_length=200)
    def __str__(self):
        return self.motivo

class Congenere(models.Model):
    congenere = models.CharField(max_length=300)
    def __str__(self):
        return self.congenere

class Detalhe(models.Model):
    comentario_perda = models.CharField(max_length=300)
    def __str__(self):
        return self.comentario_perda

class Protocolos(models.Model):
    regional = models.ForeignKey(Regional, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    comercial = models.ForeignKey(Comercial, on_delete=models.CASCADE)
    corretor = models.CharField(max_length=250)
    primeira_cotacao = models.BooleanField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=250)
    premio = models.IntegerField()
    ultima_alteracao = models.DateField(auto_now=True)
    recebimento = models.DateField()
    vencimento = models.DateField()
    fechamento = models.DateField()
    tipo_de_seguro = models.ForeignKey(TipodeSeguro, on_delete=models.CASCADE)
    expectativa = models.ForeignKey(Expectativa, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    subscritor = models.CharField(max_length=250)
    motivo_perda = models.ForeignKey(MotivoPerda, on_delete=models.CASCADE, null=True, blank=True)
    congenere = models.ForeignKey(Congenere, on_delete=models.CASCADE, null=True, blank=True)
    comentario_perda = models.CharField(max_length=250, null=True, blank=True)
    historico_1 = models.CharField(max_length=4000, null=True, blank=True)
    historico_2 = models.CharField(max_length=4000, null=True, blank=True)
    historico_3 = models.CharField(max_length=4000, null=True, blank=True)
    historico_4 = models.CharField(max_length=4000, null=True, blank=True)
    historico_5 = models.CharField(max_length=4000, null=True, blank=True)
    historico_6 = models.CharField(max_length=4000, null=True, blank=True)
    historico_7 = models.CharField(max_length=4000, null=True, blank=True)
    historico_8 = models.CharField(max_length=4000, null=True, blank=True)
    historico_9 = models.CharField(max_length=4000, null=True, blank=True)
    historico_10 = models.CharField(max_length=4000, null=True, blank=True)

