# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from login.models import UserExtended, Companies


# Base Models
class Regionals(models.Model):
    regional = models.CharField(max_length=200)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return self.regional

    class Meta:
        db_table = 'regionals'


class Subsidiaries(models.Model):
    subsidiary = models.CharField(max_length=200)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return self.subsidiary

    class Meta:
        db_table = 'subsidiaries'


class Commercials(models.Model):
    commercial = models.CharField(max_length=200)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return self.commercial

    class Meta:
        db_table = 'commercials'


class Products(models.Model):
    product = models.CharField(max_length=200)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return self.product

    class Meta:
        db_table = 'products'


class InsuranceType(models.Model):
    type = models.CharField(max_length=200)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)

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
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)

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


# Relational Models
class RegionalsAccessedBy(models.Model):
    user = models.ForeignKey(UserExtended, on_delete=models.CASCADE)
    regionals = models.ForeignKey(Regionals, on_delete=models.CASCADE)

    class Meta:
        db_table = 'regionals_accessed_by'


class SubsidiariesAccessedBy(models.Model):
    user = models.ForeignKey(UserExtended, on_delete=models.CASCADE)
    subsidiaries = models.ForeignKey(Subsidiaries, on_delete=models.CASCADE)

    class Meta:
        db_table = 'subsidiaries_accessed_by'