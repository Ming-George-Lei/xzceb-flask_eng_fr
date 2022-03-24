import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglist(unittest.TestCase): 
    def testNullInput(self):
        with self.assertRaises(ValueError):
            french_to_english(None)

    def testBonjour(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
       


class TestEnglistToFrench(unittest.TestCase): 
    def testNullInput(self):
        with self.assertRaises(ValueError):
            english_to_french(None)

    def testHello(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") 
       

unittest.main()