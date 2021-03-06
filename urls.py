from django.conf.urls.defaults import *
from django.conf import settings
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^field/', include('field.urls')),
    (r'^model/', include('model.urls')),
    (r'^application/', include('application.urls')),
    (r'^project/', include('project.urls')),
    (r'^form/', include('form.urls')),
    #(r'^view/', include('model.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    (r'^accounts/', include('registration.backends.default.urls')),

)

urlpatterns += patterns('django.views.generic.simple',
    (r'^$', 'redirect_to', {'url': '/project/list/'}),
    url(r'^screenshot/$', 'direct_to_template', {'template': 'screenshot.html'}, name='screenshot'),
)

if settings.DEBUG:
    urlpatterns+= patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':os.path.join(settings.PROJECT_PATH,'static/')}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':os.path.join(settings.PROJECT_PATH,'media/')}),
    )

