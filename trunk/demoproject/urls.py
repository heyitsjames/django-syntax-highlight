from django.conf.urls.defaults import *
import os



urlpatterns = patterns('',

    (r'^$', 'views.demo'),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root':  os.path.join(os.path.dirname(__file__), 'media').replace('\\', '/')}),
 
)
