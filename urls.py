#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',

    # RapidSMS core URLs.
    url(r'^$', 'rapidsms.views.dashboard', name='rapidsms-dashboard'),
    (r'^account/', include('rapidsms.urls.login_logout')),

    # Django admin.
    (r'^admin/', include(admin.site.urls)),

    # RapidSMS contrib app URLs.
    (r'^ajax/',       include('rapidsms.contrib.ajax.urls')),
    (r'^export/',     include('rapidsms.contrib.export.urls')),
    (r'^httptester/', include('rapidsms.contrib.httptester.urls')),
    (r'^locations/',  include('rapidsms.contrib.locations.urls')))


# helper URLs file that automatically serves the 'static' folder in
# INSTALLED_APPS via the Django static media server. (NOT for use in
# production.)
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^', include('rapidsms.urls.static_media')),
    )
