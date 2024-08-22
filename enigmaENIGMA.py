

from rotorENIGMA import Rotor


class Enigma:
    def __init__(self, shift1 = 0, shift2 = 0, low = 0x20, high = 0x7E):
        self.low = low
        self.high = high
        self.rotor1 = Rotor(shift=shift1, low=self.low, high=self.high)
        self.rotor2 = Rotor(shift=shift2, low=self.low, high=self.high)
    
    def set_initial(self, shift1, shift2):
        self.rotor1 = Rotor(shift=shift1, low=self.low, high=self.high)
        self.rotor2 = Rotor(shift=shift2, low=self.low, high=self.high)
    
    def input(self, char, decrypt=False):
        c1 = self.rotor1.get_char(self.rotor1[char]-2*decrypt*self.rotor1.shift)
        c2 = self.rotor2.get_char(self.rotor2[c1]-2*decrypt*self.rotor2.shift)
        self.rotor1 + 1
        if self.rotor1.full_rotation:
            self.rotor2 + 1
        return c2
    
    def encrypt(self, message, shift1=0, shift2=0):
        self.set_initial(shift1, shift2)
        result = ""
        for char in message:
            result += self.input(char)
        return result
    
    def decrypt(self, message, shift1=0, shift2=0):
        self.set_initial(shift1, shift2)
        result = ""
        for char in message:
            result += self.input(char, decrypt=True)
        return result