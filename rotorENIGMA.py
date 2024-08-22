


class Rotor:
    def __init__(self, shift = 0, low = 0x20, high = 0x7E):
        self.low = low
        self.high = high
        self.rotator = [chr(i) for i in range(self.low, self.high+1)]
        self.shift = shift
        self.iter_index = 0
        self.full_rotation = False
        
    def __add__(self, shift=1):
        self.shift = (self.shift + shift) % (self.high-self.low + 1)
        self.rotated(shift)
        return self.get_char(0)
    
    def __radd__(self, shift):
        return self.__add__(shift)
    
    def __sub__(self, shift=1):
        self.shift = (self.shift - shift) % (self.high-self.low + 1)
        self.rotated(-shift)
        return self.get_char(0)
    
    def __rsub__(self, shift):
        return self.__sub__(shift)
    
    def rotated(self, shift):
        if shift > 0:
            self.full_rotation = self.shift % (self.high-self.low + 1) == 0
        elif shift < 0:
            self.full_rotation = self.shift % (self.high-self.low + 1) == self.high-self.low
        return self.full_rotation
    
    def __getitem__(self, character):
        char_pos = self.rotator.index(character)
        return char_pos

    def get_char(self, index):
        return self.rotator[(index+self.shift)%(self.high-self.low + 1)]
    
    def __str__(self, shift=True):
        return "".join(self.rotator[self.shift%(self.high-self.low + 1):])+"".join(self.rotator[:self.shift%(self.high-self.low + 1)])
    
    def __len__(self):
        return len(self.rotator)
    
    # Iterator
    def __iter__(self):
        self.rot_list = list(self.rotator[self.shift%(self.high-self.low + 1):]+self.rotator[:self.shift%(self.high-self.low + 1)])
        return self

    def __next__(self):
        self.__iter__()
        if self.iter_index < self.__len__():
            self.iter_index += 1
            if self.iter_index == self.__len__():
                self.full_rotation=True
            return self.rot_list[self.iter_index-1]
        raise StopIteration
