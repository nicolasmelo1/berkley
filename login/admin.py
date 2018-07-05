# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Companies, Profiles, UserExtended

admin.site.register(UserExtended)
admin.site.register(Profiles)
admin.site.register(Companies)
# Register your models here.
