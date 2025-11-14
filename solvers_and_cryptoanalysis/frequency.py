from ciphers.monoalphabetic import monoalphabetic_cipher
from solvers_and_cryptoanalysis.checking import letter_freq_vector, PP_freq
from random import shuffle



def freq_solve(ciphertext: str, max_attempts: int =1000):
    ciphertext = ciphertext.upper()
    cipher = monoalphabetic_cipher(ciphertext)
    
    plaintext = cipher.solve(key)
    return plaintext
    

def cli():
    ciphertext = input("Please input the cipher text:\n")
    print(freq_solve(ciphertext))

if __name__ == "__main__":
    cli()