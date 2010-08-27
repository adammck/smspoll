#!/usr/bin/env python
# vim: et ts=4 sw=4


from django.contrib import admin
from . import models


admin.site.register(models.Governorate)
admin.site.register(models.District)
admin.site.register(models.Option)
admin.site.register(models.Vote)
