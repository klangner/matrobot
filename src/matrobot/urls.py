from django.conf.urls.defaults import patterns, include, url
import os

urlpatterns = patterns('',
    url(r'^$', 'matrobot.public.views.index'),
    (r'^people/', include('matrobot.people.urls')),    
    (r'^project/', include('matrobot.project.urls')),    
    (r'^public/', include('matrobot.public.urls')),    

    # System URLs
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), 'templates/media/')}),
)
