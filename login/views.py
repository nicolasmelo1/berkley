# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return render(request, 'login/login.html', {'login_message': 'Esse usuário não existe'})
        else:
            return render(request, 'login/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/auth/login/')
