from .base_cipher import Cipher
from math import log

"""
Most of the code here is a direct adaptation of National Cipher Challenge decryption 
"""


class vignere_cipher(Cipher):
    def solve(self, key:str) -> str:
        """
        Solve a vignere cipher
        Params:
            - key: The encryption/decryption key
        """
        plaintext = ''
         for i in range(len(ciphertext)):
             p = ALPHABET.index(ciphertext[i])
             k = ALPHABET.index(key[i%len(key)])
             c = (p - k) % 26
             plaintext += ALPHABET[c]
         return plaintext

    
    def autosolve(self, englishkey=False) -> str | None:
        pass