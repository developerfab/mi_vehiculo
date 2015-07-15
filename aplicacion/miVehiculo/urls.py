from django.conf.urls import include, url, patterns
from django.contrib import admin
from miVehiculo import views

urlpatterns = patterns(
	'',
	url(r'^$', views.index, name="index"),
	url(r'^login/$', views.loginView, name="login"),
	url(r'^logout/$', views.logoutView, name="logout"),
	url(r'^home/$', views.home, name="home"),
	url(r'^impuesto/$', views.misImpuestos, name="impuesto")
)