from .base_cipher import Cipher
from string import ascii_uppercase

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
             p = ascii_uppercase.index(ciphertext[i])
             k = ascii_uppercase.index(key[i%len(key)])
             c = (p - k) % 26
             plaintext += ascii_uppercase[c]
         return plaintext

    
    def autosolve(self, period=None:int | None, englishkey=False:bool) -> str | None:
        raise NotImplementedError
