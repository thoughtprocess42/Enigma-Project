from decodeENIGMA import CrackCode

if __name__ == "__main__":
    test = CrackCode("/Users/ethan/Downloads/Encrypt.txt", "/Users/ethan/Downloads/Frequencies.txt")
    shift1, shift2, message = test.decrypt()
    print(f"Rotor 1 initial position: {shift1}")
    print(f"Rotor 2 initial position: {shift2}")
    print(f"Decrypted Message:\n{message}")
    print(f"Rotor 1 initial position: {shift1}") 
    print(f"Rotor 2 initial position: {shift2}")