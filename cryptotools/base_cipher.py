from string import ascii_uppercase

class cipher:
    def __init__(self, ciphertext:str):
        self.ciphertext = ciphertext.upper()
        values = {}
        for letter in ascii_uppercase:
            values.update({letter: self.ciphertext.count(letter)/len(self.ciphertext.replace(" ", ""))})
        self.frequencies = values