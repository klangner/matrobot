from django.conf.urls.defaults import patterns


urlpatterns = patterns('matrobot.public.views',
    (r'^datasets$', 'datasets'),
)

