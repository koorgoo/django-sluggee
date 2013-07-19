from django.test import SimpleTestCase
from django.utils.six import u
from sluggee.utils import slugify
from .en_en import CASES as EN_EN
from .ru_en import CASES as RU_EN
from .ruen_en import CASES as RUEN_EN


class SlugifyTestCase(SimpleTestCase):
    def assertCases(self, cases):
        for key in cases.keys():
            expected = key
            actual = slugify(cases[key])
            self.assertEqual(expected, actual, '%s != %s' % (expected, actual))

    def test_english_cases(self):
        self.assertCases(EN_EN)

    def test_russian_cases(self):
        self.assertCases(RU_EN)

    def test_russian_english_mix_cases(self):
        self.assertCases(RUEN_EN)
