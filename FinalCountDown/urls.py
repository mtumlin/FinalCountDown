from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^', include('countdown.urls', namespace="countdown")),
                       url(r'^admin/', include(admin.site.urls)),
)
