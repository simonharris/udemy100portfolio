import unittest

from morse import encode

class MorseTest(unittest.TestCase):

    def test_phases(self):
        self.assertEqual(encode('s'), '...')
        self.assertEqual(encode('sos'), '...---...')
        self.assertEqual(encode('2025/04/28'), 
                         '..--------..---.....-..-.-----....--..-...------..')