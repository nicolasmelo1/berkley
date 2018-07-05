# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class EmailBackend:
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = UserExtended
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if getattr(user, 'is_active', False) and user.check_password(password):
                return user
        return None


class Companies(models.Model):
    name = models.CharField(max_length=400)

    class Meta:
        db_table = 'companies'


class Profiles(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'profiles'


class UserExtended(AbstractUser):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE)

    class Meta:
        db_table = 'users'
