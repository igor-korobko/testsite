from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('polls.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^userprofile/', include('userprofile.urls', namespace="userprofile")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)