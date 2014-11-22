from django.conf.urls import patterns, include, url
from app import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^lower$', views.LowerIndexView.as_view(), name='lower_index'),
    url(r'^lower/(?P<lower_id>\d+)/$', views.LowerDetailView, name='lower_detail'),
    url(r'^client$', views.ClientIndexView.as_view(), name='client_index'),
    url(r'^client/(?P<client_id>\d+)/$', views.ClientDetailView, name='client_detail'),
    #url(r'^hello/$', TemplateView.as_view(template_name="client_info.html")),
)
