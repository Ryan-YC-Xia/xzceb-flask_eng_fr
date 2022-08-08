import unittest
from translator import english_to_french, french_to_english

class TestsTranslator(unittest.TestCase):
    def test_e2f(self):
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_f2e(self):
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()