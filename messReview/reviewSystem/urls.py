from django.conf.urls import patterns, include, url
#from django.contrib import admin
from reviewSystem import views

urlpatterns = patterns('',
	url(r'^$', views.ItemA.as_view()),
    #url(r'^$', views.hello, name='hello'),
)


	