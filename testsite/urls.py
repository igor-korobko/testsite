from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(router.urls)),

    url(r'^$', include('polls.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^userprofile/', include('userprofile.urls', namespace="userprofile")),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^social/', include('social_auth.urls')),
    url(r'^accounts/profile/$', include('polls.urls')),

    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)