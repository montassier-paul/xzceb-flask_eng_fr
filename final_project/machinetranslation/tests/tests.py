import unittest
import sys
from machinetranslation.translator import english_to_french, french_to_englich

class TestTranslationMethods(unittest.TestCase):

    def test_english_to_french_null(self):
        self.assertEqual(english_to_french(' ')["translations"][0]["translation"], ' ')

    def test_english_to_french_Hello(self):
        self.assertEqual(english_to_french('Hello')["translations"][0]["translation"], 'Bonjour')

    def test_french_to_englich_null(self):
        self.assertEqual(french_to_englich(' ')["translations"][0]["translation"], ' ')

    def test_french_to_englich_Bonjour(self):
        self.assertEqual(french_to_englich('Bonjour')["translations"][0]["translation"], 'Hello')  

    

if __name__ == '__main__':
    unittest.main()