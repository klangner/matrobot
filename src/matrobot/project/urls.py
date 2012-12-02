from django.conf.urls.defaults import patterns


urlpatterns = patterns('matrobot.project.views',
    (r'^', 'index'),
    (r'long_term^', 'long_term'),
)

