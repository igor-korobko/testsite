from django.conf.urls import patterns, include, url
from userprofile import views


urlpatterns = patterns('',
    url(r'^user/$', views.user_, name='user'),
    url(r'^register/$', views.register_, name='register'),
    url(r'^(?P<user_name>\w+)/public/$', views.public_, name='public'),
    url(r'^login/$', views.login_, name='login'),
    url(r'^logout/$', views.logout_, name='logout'),
)
