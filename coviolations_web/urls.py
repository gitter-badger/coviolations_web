from django.conf.urls import patterns, include, url
from django.contrib import admin
from .api import v1_api


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('app.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
