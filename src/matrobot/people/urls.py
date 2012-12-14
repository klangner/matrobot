from django.conf.urls.defaults import patterns


urlpatterns = patterns('matrobot.people.views',
    (r'^$', 'index'),
)

