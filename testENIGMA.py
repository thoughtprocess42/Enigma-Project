import unittest
from rotorENIGMA import Rotor
from enigmaENIGMA import Enigma
from decodeENIGMA import CrackCode

class EncryptionTest(unittest.TestCase):
    def test_Rotor(self):
        rotor = Rotor()
        rotor + 5
        self.assertEqual(rotor.get_char(rotor["a"]), "f")
    
    def test_EnigmaEncrypt(self):
        enigma = Enigma()
        message = enigma.encrypt("abCD")
        self.assertEqual(message, "acEG")
    
    def test_EnigmaDecrypt(self):
        enigma = Enigma()
        message = enigma.decrypt("acEG")
        self.assertEqual(message, "abCD")
    
    def test_chi_squared(self):
        crack = CrackCode("/Users/ethan/Downloads/Encrypt.txt", "/Users/ethan/Downloads/Frequencies.txt")
        delta = 0.01
        self.assertAlmostEqual(crack.chi_squared(crack.encrypted[:100]), 24.73, delta=delta)

if __name__ == "__main__":
    unittest.main()