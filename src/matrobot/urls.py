from django.conf.urls.defaults import patterns, include, url
import os

urlpatterns = patterns('',
    # Homepage
    url(r'^$', 'matrobot.public.views.index'),
    (r'^project/', include('matrobot.project.urls')),    

    # System URLs
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), 'templates/media/')}),
)
