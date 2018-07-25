# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from berkley.defaults import PermissionHandler

from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        permissions = PermissionHandler(user)
        if user:
            login(request, user)
            company = permissions.get_user_company()
            return redirect('/{}/pipeline/'.format(company.endpoint))
        else:
            return render(request, 'login/login_base.html', {'login_message': 'Esse usuário não existe'})
    else:
        return render(request, 'login/login_base.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/auth/login/')
