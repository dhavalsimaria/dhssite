from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contact/add/$', views.add, name='add'),
	url(r'^downloadCV/$', views.download, name='download')
]