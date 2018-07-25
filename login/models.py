# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class EmailBackend:
    """
    User logs in using email and password as default, not by
    username and password.
    """
    def authenticate(self, request,  username=None, password=None):
        try:
            user = UserExtended.objects.get(email=username, is_active=True)
        except UserExtended.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return UserExtended.objects.get(id=user_id)
        except UserExtended.DoesNotExist:
            return None


class Companies(models.Model):
    name = models.CharField(max_length=400, default=None)
    documentId = models.CharField(max_length=250, default=None)
    endpoint = models.CharField(max_length=280, default=None)
    phone = models.CharField(max_length=250, default=None)
    cellphone = models.CharField(max_length=250, default=None)
    street = models.CharField(max_length=500, default=None)
    county = models.CharField(max_length=250, default=None)
    address_number = models.IntegerField(default=None)
    address_complement = models.CharField(max_length=500, default=None)
    postal_code = models.CharField(max_length=250, default=None)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'companies'


class Profiles(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, default=None)
    can_edit = models.BooleanField(default=False)

    class Meta:
        db_table = 'profiles'


class UserExtended(AbstractUser):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, default=None)
    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE, default=None)
    phone = models.CharField(max_length=250, default=None)
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'
