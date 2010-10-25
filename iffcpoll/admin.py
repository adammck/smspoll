#!/usr/bin/env python
# vim: et ts=4 sw=4


from django.contrib import admin
from django.contrib.admin import sites
from . import models

try:
    admin.site.register(models.Governorate)
    admin.site.register(models.District)
    admin.site.register(models.Option)
    admin.site.register(models.Vote)

# catch exceptions, to allow this module to be imported multiple times
# without exploding. (urls.py and nose both import it during testing.)
except sites.AlreadyRegistered:
    pass
