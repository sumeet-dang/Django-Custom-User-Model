from django.conf.urls import url
from django.views.generic import TemplateView
from core.views import home

urlpatterns = [
    url(r'^$',home,name='index'),
]
