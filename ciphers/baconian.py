lookup = {
    "A": "AAAAA", "B": "AAAAB",
    "C": "AAABA", "D": "AAABB",
    "E": "AABAA", "F": "AABAB",
    "G": "AABBA", "H": "AABBB",
    "I": "ABAAA", "J": "ABAAA",
    "K": "ABAAB", "L": "ABABA",
    "M": "ABABB", "N": "ABBAA",
    "O": "ABBAB", "P": "ABBBA",
    "Q": "ABBBB", "R": "BAAAA",
    "S": "BAAAB", "T": "BAABA",
    "U": "BAABB", "V": "BAABB",
    "W": "BABAA", "X": "BABAB",
    "Y": "BABBA", "Z": "BABBB"
}


def decrypt(ciphertext: str):
    """Decrypt ciphertext using the bacanian cipher"""
    decipher = ''
    x = 0
    while x < len(ciphertext):
        if ciphertext[x] != ' ':
            substr = ciphertext[x:x + 5]  # makes a substring 5 letters long if there is acc smth in that index
            keys_list = list(lookup.keys())
            values_list = list(lookup.values())
            decipher += keys_list[values_list.index(substr)]  # finds which letter matches that 5 letter substring and adds it to decipher string
            x += 5
        else:
            decipher += ' '
            x += 1  # skip a space
    print(decipher)


solve = decrypt

if __name__ == "__main__":
    cipher = input("Cipher text: ").upper()
    decrypt(cipher)
