from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'matrobot.public.views.index'),
    (r'^people/', include('matrobot.people.urls')),    
    (r'^project/', include('matrobot.project.urls')),    
    (r'^public/', include('matrobot.public.urls')),    
)
