#!/usr/bin/env python
# vim: et ts=4 sw=4


from django.test import TestCase
from .utils import extract_option
from .models import Option


class OptionExtractor(TestCase):
    fixtures = ["test_data"]

    def setUp(self):
        self.red = Option.objects.get(pk=1)

    def test_extract_type_failure(self):
        """
        Check that extract_option raises TypeError when called with
        anything other than a basestring.
        """

        for obj in [True, None, object]:
            self.assertRaises(TypeError, extract_option, obj)

    def test_extract_value_failure(self):
        """
        Check that extract_option raises ValueError when called with
        a string which does not match any Option.
        """

        for text in ["jibberish", "!@#$%^&*"]:
            self.assertRaises(ValueError, extract_option, text)

    def test_simple_extract(self):
        """
        Check that extract_option can extract simple submissions, which
        contain only the caption or letter of the Option.
        """

        for text in ["RED", "Red", "red", "R", "r"]:
            self.assertEqual(extract_option(text), self.red)

    def test_almost_caption_extract(self):
        """
        Check that extract_option forgives spelling mistakes.
        """

        for text in ["rud", "rrred", "red!"]:
            self.assertEqual(extract_option(text), self.red)
