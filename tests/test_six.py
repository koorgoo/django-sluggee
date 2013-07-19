# -*- coding: utf-8 -*-
from django.test import SimpleTestCase
from sluggee.six import u, PY3


class SixTestCase(SimpleTestCase):
    def assertUnicode(self, c):
        if PY3: self.assertTrue(isinstance(c, str))
        else: self.assertTrue(isinstance(c, unicode))

    def test_english_to_unicode(self):
        self.assertUnicode(u('d'))

    def test_russian_to_unicode(self):
        self.assertUnicode(u('ю'))

