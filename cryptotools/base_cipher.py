from string import ascii_uppercase
from collections import Counter

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