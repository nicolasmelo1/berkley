# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Regional, Comercial, Filial, Produto, TipodeSeguro, Expectativa, Status, MotivoPerda, Protocolos
from django.contrib import admin

admin.site.register(Regional)
admin.site.register(Comercial)
admin.site.register(Filial)
admin.site.register(Produto)
admin.site.register(TipodeSeguro)
admin.site.register(Expectativa)
admin.site.register(Status)
admin.site.register(MotivoPerda)
admin.site.register(Protocolos)
# Register your models here.
