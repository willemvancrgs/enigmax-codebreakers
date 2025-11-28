from string import ascii_uppercase
from collections import Counter
from math import log
from .checking import TETRAGRAMS

class Cipher:
    def __init__(self, ciphertext: str):
        self.ciphertext = ciphertext.upper()
        # keep only letters once, and compute counts in one pass
        cleaned = [c for c in self.ciphertext if c.isalpha()]
        total = len(cleaned)
        counts = Counter(cleaned)
        # build frequencies dict explicitly (avoids update overload ambiguity)
        self.frequencies = {
            letter: (counts.get(letter, 0) / total) if total else 0.0
            for letter in ascii_uppercase
        }

    
    def fitness(self, text=self.ciphertext) -> float:
        result = 0
        for i in range(len(text)-3):
            tetragram = text[i:i+4]
            x = (
                ascii_uppercase.index(tetragram[0])*26*26*26 +
                ascii_uppercase.index(tetragram[1])*26*26 +
                ascii_uppercase.index(tetragram[2])*26 +
                ascii_uppercase.index(tetragram[3]))
            y = TETRAGRAMS[x]
            if y == 0:
                result += -15
            else:
                result += log(y)
        result = result / (len(text) - 3)
        return result