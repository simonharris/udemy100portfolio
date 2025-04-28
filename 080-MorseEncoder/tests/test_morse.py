import unittest

from morse import encode

class MorseTest(unittest.TestCase):

    def test_phases(self):
        self.assertEqual(encode('s'), '...')
        self.assertEqual(encode('sos'), '...---...')
        self.assertEqual(encode('2025/04/28'),
                         '..--------..---.....-..-.-----....--..-...------..')

    def test_case_insensitive(self):
        self.assertEqual(encode('morsecode'), '-----.-.....-.-.----...')
        self.assertEqual(encode('mOrSeCoDe'), '-----.-.....-.-.----...')

    def test_missing_characters(self):
        with self.assertRaises(Exception) as _:
            encode('Rod, Jane & Freddy')
