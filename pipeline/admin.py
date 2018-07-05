# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Regionals, Commercials, Subsidiaries, Products, InsuranceType, Expectations, Status, ReasonsForLoss, Congeners
from django.contrib import admin

admin.site.register(Regionals)
admin.site.register(Commercials)
admin.site.register(Subsidiaries)
admin.site.register(Products)
admin.site.register(InsuranceType)
admin.site.register(Expectations)
admin.site.register(Status)
admin.site.register(ReasonsForLoss)
admin.site.register(Congeners)
# Register your models here.
