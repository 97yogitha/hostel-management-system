from django.conf.urls import url , include
from . import views

app_name = 'info'

urlpatterns = [
	 url(r'^$', views.index, name='index'),
	 url(r'^register/$', views.register, name='register'),
	 url(r'^login_user/$', views.login_user, name='login_user'),
	 url(r'^logout_user/$', views.logout_user, name='logout_user'),
	 url(r'^login_admin/$', views.login_admin, name='login_admin'),
	 url(r'^logout_admin/$', views.logout_admin, name='logout_admin'),
	 url(r'^login_mess/$', views.login_mess, name='login_mess'),
	 url(r'^logout_mess/$', views.logout_mess, name='logout_mess'),
	 url(r'^complaint_register/$',views.complaint_register, name ='complaint_register'),
	 url(r'^complaint_view/$',views.complaint_view, name ='complaint_view'),
	 url(r'^complaint_admin/$',views.complaint_admin,name= 'complaint_admin'),
	 url(r'^menu_update/$',views.menu_update,name ='menu_update'),
	 url(r'^menu_view/$',views.menu_view,name='menu_view'),
	 url(r'^student_menu_view/$',views.student_menu_view,name='student_menu_view'),
	 url(r'^student_profile/$',views.student_profile,name='student_profile'),
	 # url(r'^update_profile/$',views.UpdateStudentProfile.as_view(),name='update_profile'),
	 # url(r'^update_profile/(?P<pk>[0-9]+)/$', views.UpdateStudentProfile.as_view(), name='update_student_profile'), 
	 # url(r'^update_profile/(?P<roll_no>[a-z0-9A-Z]+)/$', views.updateprofile_new, name='updateprofile_new'),
	 url(r'^update_profile/$', views.updateprofile_new, name='updateprofile_new'), 
	 url(r'^admin_profile/$',views.admin_profile,name='admin_profile'),
	 url(r'^mess_profile/$',views.mess_profile,name='mess_profile'),
]