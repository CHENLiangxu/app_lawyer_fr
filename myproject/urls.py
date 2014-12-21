from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from app import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^lower$', views.LowerIndexView.as_view(), name='lower_index'),
    url(r'^lower/(?P<lower_id>\d+)/$', views.lowerDetailView, name='lower_detail'),
    url(r'^lower_create$', views.CreateLowerView, name='lower_create'),
    url(r'^appointment$', views.AppointmentIndexView.as_view(), name='appointment_index'),
    url(r'^appointment/(?P<appointment_id>\d+)/$', views.AppointmentDetailView, name='appointment_detail'),
    url(r'^appointment_create$', views.CreateAppointmentView, name='appointment_create'),
    url(r'^target_user$', views.TargetUserIndexViews.as_view(), name='target_user_index'),
    url(r'^target_user/(?P<target_user_id>\d+)/$', views.TargetUserDetailView, name='target_user_detail'),
    url(r'^target_user_create$', views.CreateTargetUserView, name='target_user_create'),
    url(r'^user_create$', views.CreateUserView, name='user_create'),
    url(r'^test$', views.my_view),
    url(r'^login$', views.LoginView, name='login'),
    url(r'^logout$', views.LogoutView, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
