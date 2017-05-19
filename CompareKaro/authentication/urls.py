from django.conf.urls import url
from django.views.generic import TemplateView
from authentication.views import create_profile,log_out,log_in

urlpatterns = [
    url(r'^register/$',create_profile,name="register"),
    url(r'^logout/$', log_out, name='logout'),
    url(r'^login/$', log_in ,name='login')
]
