from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from app import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^lower$', views.LowerIndexView.as_view(), name='lower_index'),
    url(r'^lower/(?P<lower_id>\d+)/$', views.lowerDetailView, name='lower_detail'),
    url(r'^lower_create$', views.CreateLowerView, name='lower_create'),
    url(r'^client$', views.ClientIndexView.as_view(), name='client_index'),
    url(r'^client/(?P<client_id>\d+)/$', views.clientDetailView, name='client_detail'),
    url(r'^client_create$', views.CreateClientView, name='client_create'),
    url(r'^test$', views.my_view),
    #url(r'^hello/$', TemplateView.as_view(template_name="client_info.html")),
)
