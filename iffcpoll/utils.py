#!/usr/bin/env python
# vim: et ts=4 sw=4


from djappsettings import settings
from .models import Option


def distance(str_one, str_two):
    """
    Return the absolute levenshtein distance of two strings, or None if
    the Levenshtein package isn't available.
    """

    try:
        from Levenshtein import distance
        return distance(str_one, str_two)

    except ImportError:
        return None


def extract_option(text):
    """
    Return the Option referenced by ``text`` (in various fuzzy ways), or
    raise a ValueError if none could be found. This function tries hard
    to find an Option, as sort-of documented by the ``tests`` module.
    """

    if not isinstance(text, basestring):
        raise TypeError("Not a basestring: %r" % text)

    t = unicode(text).lower()
    matches = []

    for option in Option.objects.all():
        l = option.letter.lower()
        c = option.caption.lower()

        # return early if this is an exact match.
        if (t == l) or (t == c):
            return option

        # otherwise, compile a list of distances.
        d = distance(t, c)
        if (d is not None) and (d <= settings.MAX_MATCH_DISTANCE):
            matches.append((option, d))

    # return the closest option.
    if len(matches):
        m = sorted(matches, key=lambda x: x[1])
        return m[0][0]

    raise ValueError("No Option could be found in: %s" % text)
