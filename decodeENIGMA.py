import re
from collections import Counter
from enigmaENIGMA import Enigma


class CrackCode:
    def __init__(self, message_file, freq_file, brief=50, deep=2000):
        self.common_words = set(["the", "be", "to", "of", "and", "in", "that", "have", "i"])
        
        with open(message_file, "r") as file:
            self.encrypted = file.read()

        with open(freq_file, "r") as file:
            freq = file.read()
        keys = re.findall(r'character\[\s*(.)\s*\]\s*=', freq)
        values = [int(val) for val in re.findall(r'= frequency\[\s*(\d+)\s*\]', freq)]
        expected_val = [val/sum(values) for val in values]
        self.expected_freq = dict(zip(keys, expected_val))
        
        self.brief = brief
        self.deep = deep
        self.enigma = Enigma()
        self.likely = []
        self.likely_chi_squared = []
    
    def brief_test(self):
        for shift1 in range(0, self.enigma.high-self.enigma.low+1):
            for shift2 in range(0, self.enigma.high-self.enigma.low+1):
                message = self.enigma.decrypt(self.encrypted[:self.brief], shift1=shift1, shift2=shift2)
                if bool(set([word.lower() for word in message.split(" ")]) & self.common_words):
                    self.likely.append((shift1, shift2))
    
    def deep_test(self):
        for shift1, shift2 in self.likely:
            message = self.enigma.decrypt(self.encrypted[:self.deep], shift1=shift1, shift2=shift2)
            self.chi_squared(message)
    def find_solution(self):
        min_index = sorted(enumerate(self.likely_chi_squared), key=lambda pair: pair[1])[0]
        shift1, shift2 = self.likely[min_index[0]]
        message = self.enigma.decrypt(self.encrypted, shift1=shift1, shift2=shift2)
        return shift1, shift2, message

    def chi_squared(self, message):
        chi_sq = 0
        length = len(message)
        freq = Counter(message)
        for char in freq:
            expected = self.expected_freq.get(char, 0) * length
            if expected > 5:
                chi_sq += (freq[char]-expected)**2/expected
        self.likely_chi_squared.append(chi_sq)
        return chi_sq
    
    def decrypt(self):
        self.brief_test()
        self.deep_test()
        return self.find_solution()


