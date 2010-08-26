#!/usr/bin/env python
# vim: et ts=4 sw=4


from django.db import models
from rapidsms.contrib.locations.models import Location


class Governorate(Location):
    name = models.CharField(max_length=100)
