#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from rapidsms.contrib.handlers.handlers.base import BaseHandler
from ..models import Option, Vote


class IffcHandler(BaseHandler):
    """
    This handler watches for incoming votes, by matching them against
    Option instances. Since these votes are probably submitted by the
    general public (not trained reporters), many variations of the
    option are accepted::

      >>> IffcHandler.test("a")
      [u'Thank you. What is your age, gender, and district?']

    Only a single vote is accepted from each Connection, so we assume
    that the second incoming message is a response to the demographic
    request. Ideally, it is in the form ``[age] [gender] [location]``::

      >>> IffcHandler.test("10 male baghdad")
      [u'Thank you.']

    But as above, many variations on are accepted. See ``tests.py`` for
    a comprehensive list of accepted patterns, or ``utils.py`` for the
    parser implementation).

    Once the demographic information has been submitted, the Connection
    is not allowed to vote again.

      >>> IffcHandler.test("b")
      [u'You have already voted.']

    NOTE: This handler could/should be implemented as two (or more)
    separate classes, but RapidSMS handlers are only easy to test in
    isolation (via the BaseHandler.test method). Once scripted testing
    is fixed and packaged, this handler might be split up.
    """

    @classmethod
    def dispatch(cls, router, msg):
        for option in Option.objects.all():
            if msg.text == option.letter:
                inst = cls(router, msg)
                inst.handle(option)
                return True

    def handle(self, option):
        if Vote.objects.filter(connection=self.msg.connection):
            return self.respond("You have already voted.")

        vote = Vote.objects.create(
            connection=self.msg.connection,
            option=option)

        return self.respond(
            "Thank you for voting: %(vote)s.",
            vote=vote.option.letter.upper())
