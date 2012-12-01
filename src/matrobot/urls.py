from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import os

admin.autodiscover()

urlpatterns = patterns('',
    # Homepage
    url(r'^$', 'matrobot.public.views.index'),
    (r'^project/', include('matrobot.project.urls')),    

    # System URLs
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), 'templates/media/')}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)
