# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Regionals(models.Model):
    regional = models.CharField(max_length=200)

    def __str__(self):
        return self.regional

    class Meta:
        db_table = 'regionals'


class Subsidiaries(models.Model):
    subsidiary = models.CharField(max_length=200)

    def __str__(self):
        return self.subsidiary

    class Meta:
        db_table = 'subsidiaries'


class Commercials(models.Model):
    commercial = models.CharField(max_length=200)

    def __str__(self):
        return self.commercial

    class Meta:
        db_table = 'commercials'


class Products(models.Model):
    product = models.CharField(max_length=200)

    def __str__(self):
        return self.product

    class Meta:
        db_table = 'products'


class InsuranceType(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'insurance_types'


class Expectations(models.Model):
    expectation = models.CharField(max_length=200)

    def __str__(self):
        return self.expectation

    class Meta:
        db_table = 'expectations'


class Status(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'status'


class ReasonsForLoss(models.Model):
    reason = models.CharField(max_length=200)

    def __str__(self):
        return self.reason

    class Meta:
        db_table = 'loss_reasons'


class Congeners(models.Model):
    congener = models.CharField(max_length=300)

    def __str__(self):
        return self.congener

    class Meta:
        db_table = 'congeners'


class Detail(models.Model):
    loss_comentary = models.CharField(max_length=300)

    def __str__(self):
        return self.loss_comentary

    class Meta:
        db_table = 'loss_detail'


class History(models.Model):
    from protocolos.models import Protocols

    protocol = models.ForeignKey(Protocols, on_delete=models.CASCADE)
    history = models.CharField(max_length=4000, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'history'