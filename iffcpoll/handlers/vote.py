#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from rapidsms.contrib.handlers.handlers.base import BaseHandler
from ..models import Option, Vote


class VoteHandler(BaseHandler):
    """
    This handler watches for incoming votes, by matching them against
    Option instances. Since these votes are probably submitted by the
    general public (not trained reporters), many variations of the
    option are accepted::

      >>> VoteHandler.test("a")
      [u'Thank you for voting: A.']

    Only a single vote is accepted from each Connection. This isn't a
    terribly good way of identifying unique voters, but it's as good as
    we can reasonably expect. Subsequent votes are rejected::

      >>> VoteHandler.test("a", identity="xxx")
      [u'Thank you for voting: A.']

      >>> VoteHandler.test("b", identity="xxx")
      [u'You have already voted.']

    All other messages are ignored::

      >>> VoteHandler.test("whatever")
      False
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
