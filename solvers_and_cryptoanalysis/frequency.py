# Entirely unfinished ignore pls

from ciphers import monoalphabetic
from solvers_and_cryptoanalysis.checking import letter_freq_vector, PP_freq
from random import shuffle


def order_letter_freq(freq_vector: dict[str, int]):
    print(dict(sorted(freq_vector.items())))

def cli():
    ciphertext = input("Please input the cipher text:\n")
    print(o)


if __name__ == "__main__":
    freq_vector = PP_freq
    print(order_letter_freq(freq_vector))
    cli()