#!/usr/bin/env python
# vim: et ts=4 sw=4


from django.db import models


class IffcConnectionExtension(models.Model):
    """
    Extend the RapidSMS Connection model with demographic information.
    It might seem more obvious to attach these to a Contact, but this
    app makes no effort to support more than one human per Connection,
    so I'm putting them here to accurately model the actual situation.
    """

    GENDER_OPTIONS = (
        ("m", "Male"),
        ("f", "Female")
    )

    # we must link iffcpoll.District lazily, to avoid a circular import
    # (between rapidsms.models, this module, and iffcpoll.models).
    DISTRICT_MODEL =\
        "iffcpoll.District"

    age      = models.PositiveIntegerField(null=True, blank=True)
    gender   = models.CharField(null=True, blank=True, max_length=1, choices=GENDER_OPTIONS)
    district = models.ForeignKey(DISTRICT_MODEL, null=True, blank=True)

    class Meta:
        abstract = True

    def has_voted(self):
        return False
