from django.conf.urls import patterns, include, url
from userprofile import views

urlpatterns = patterns('',
    url(r'^user/$', views.user_, name='user'),
)
