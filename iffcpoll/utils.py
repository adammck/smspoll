#!/usr/bin/env python
# vim: et ts=4 sw=4


from .models import Option


def extract_option(text):
    """
    Return the Option referenced by ``text`` (in various fuzzy ways), or
    raise a ValueError if none could be found. This function tries hard
    to find an Option, as sort-of documented by the ``tests`` module.
    """

    for option in Option.objects.all():
        if text == option.letter:
            return ("", option, "")

    raise ValueError("No Option could be found in: %s" % text)
