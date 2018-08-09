from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', views.protocolos, name='protocolos'),
    url(r'^delete/$', views.delete, name='protocolos_delete'),
]