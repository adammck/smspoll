#!/usr/bin/env python
# vim: et ts=4 sw=4


from django.test import TestCase
from .utils import extract_option
from .models import Option


class OptionExtractor(TestCase):
    fixtures = ["test_question"]

    def setUp(self):
        self.red = Option.objects.get(pk=1)

    def test_rejcts_non_strings(self):
        for obj in [True, None, object]:
            self.assertRaises(TypeError, extract_option, obj)

    def test_rejects_junk_strings(self):
        for text in ["jibberish", "!@#$%^&*"]:
            self.assertRaises(ValueError, extract_option, text)

    def test_matches_captions_and_letters(self):
        for text in ["RED", "Red", "red", "R", "r"]:
            self.assertEqual(extract_option(text), self.red)

    def test_forgives_spelling_mistakes(self):
        for text in ["rud", "rrred", "red!"]:
            self.assertEqual(extract_option(text), self.red)
