from django.conf.urls import include, url, patterns
from django.contrib import admin
from miVehiculo import views

urlpatterns = patterns(
	'',
	url(r'^$', views.index, name="index"),
)