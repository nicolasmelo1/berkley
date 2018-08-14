from django.conf.urls import url
from .views import Pipeline, PipelineEdit, BusinessPlan
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(Pipeline.as_view()), name='pipeline'),
    url(r'^(?P<pk>\d+)/$', login_required(PipelineEdit.as_view()), name='pipeline_query'),
    url(r'^business_plan/$', login_required(BusinessPlan.as_view()), name='business_plan_add'),
]
