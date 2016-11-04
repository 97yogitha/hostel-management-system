from django.conf.urls import url , include
from . import views

app_name = 'info'

urlpatterns = [
	 url(r'^$', views.index, name='index'),
	 url(r'^register/$', views.register, name='register'),
	 url(r'^login_user/$', views.login_user, name='login_user'),
	 url(r'^logout_user/$', views.logout_user, name='logout_user'),
	 url(r'^login_admin/$', views.login_user, name='login_admin'),
	 url(r'^logout_admin/$', views.logout_user, name='logout_admin'),
	 url(r'^login_mess/$', views.login_user, name='login_mess'),
	 url(r'^logout_mess/$', views.logout_user, name='logout_mess'),
]