"""berkley URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.pipeline, name='pipeline')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='pipeline')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('(?P<company>[\w-]+)/', include([
        url(r'^protocolos/', include('protocolos.urls'), name='protocolos_app'),
        url(r'^dashboard/', include('dashboard.urls'), name='dashboard_app'),
        url(r'^pipeline/', include('pipeline.urls'), name='pipeline_app'),
    ]), name='company_includes'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls'), name='login_app'),
]
