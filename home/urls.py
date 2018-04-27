from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', views.temp, name='home'),
    url(r'^(?P<pk>\d+)/$', views.consulta, name='consulta'),
]