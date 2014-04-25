from django.conf.urls import patterns, include, url
from polls import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>\d+)$', views.detail, name='detail'),
    # url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    url(r'^vote/$', views.vote, name='vote'),
    url(r'^search/$', views.search, name='search'),
    url(r'^cookies/$', views.cookies_, name='cookies'),
)
