from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import sys

#from autocomplete.views import autocomplete
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r"^$", 'views.home', name="home"),
    url(r'^admin_tools/', include('admin_tools.urls')),
    
#    url('^autocomplete/', include(autocomplete.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)

urlpatterns += staticfiles_urlpatterns()

from django.conf import settings
if settings.DEBUG or ('test' in sys.argv):
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    )
    
urlpatterns += patterns('',
    (r'^', include('coop_agenda.urls')),
    (r'^', include('coop_cms.urls')),
)