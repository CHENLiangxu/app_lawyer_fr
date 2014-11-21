from django.conf.urls import patterns, include, url
from app import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', views.LowerIndexView.as_view(), name='lower_index'),
    url(r'^(?P<lower_id>\d+)/$', views.LowerDetailView, name='lower_detail'),
    #url(r'^hello/$', TemplateView.as_view(template_name="client_info.html")),
)
