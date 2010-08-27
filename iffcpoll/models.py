#!/usr/bin/env python
# vim: et ts=4 sw=4


from django.db import models
from rapidsms.models import Connection
from rapidsms.contrib.locations.models import Location


class Governorate(Location):
    name = models.CharField(max_length=100)


class District(Location):
    name = models.CharField(max_length=100)


class Option(models.Model):
    letter = models.CharField(max_length=1)
    caption = models.CharField(max_length=100)

    class Meta:
        ordering = ("letter",)

    def __unicode__(self):
        return "%s: %s" %\
            (self.letter.upper(), self.caption)


class Vote(models.Model):
    connection = models.ForeignKey(Connection, unique=True)
    option = models.ForeignKey(Option)

    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    district = models.ForeignKey(District, null=True, blank=True)

    def __unicode__(self):
        return "%s by %s" %\
            (self.option.letter.upper(), self.connection.identity)
