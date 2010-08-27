#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from rapidsms.contrib.handlers.handlers.base import BaseHandler
from ..models import Option, Vote


class DemographicsHandler(BaseHandler):
    """
    This handler watches for incoming demographic information. Ideally,
    it is in the form ``[age] [gender] [location]``, but many formats
    are accepted::
    
      >>> DemographicsHandler.test("10 male baghdad")
      [u'Thank you.']
    
    As usual, all other messages are ignored::

      >>> DemographicsHandler.test("whatever")
      False
    """

    @classmethod
    def dispatch(cls, router, msg):
        pass

    def handle(self, age, gender, location):
        pass
