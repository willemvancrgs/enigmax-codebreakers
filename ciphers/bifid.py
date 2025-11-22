from base_cipher import Cipher
from typing import Iterable

class BifidCipher(Cipher):
    def solve(self, key:Iterable[Iterable[str]]) -> str:
        """
        Solves the bifid cipher
        Args:
            - key: a 2D-array-like representation of a 5x5 polybias cipher where I and J occupy the same cell
        """

        validkey = True
        if len(key) != 5:
            validkey = False
        for row in key:
            if len(row) != 5:
                validkey = False
        if not validkey:
            raise ValueError("A 5x5 polybius table must be given")
        
        for row in key:
            for cell in row:
                if cell == "J":
                    cell = "I"
        
        # Convert Polybius 2D array to dictionaries for faster lookups
        coords_to_words = {(i, j): key[i][j] for i in range(5) for j in range(5)}
        words_to_coords = {value:key for key, value in coords_to_words.items()}

        coord_continuous = ""

        for character in self.ciphertext:
            for coord in words_to_coords[character]:
                coord_continuous += str(coord)
        
        rows = [coord_continuous[:len(coord_continuous)//2], coord_continuous[len(coord_continuous)//2:]]

        plaintext = ""
        
        pt_coord_list = tuple(zip(rows[0], rows[1]))

        for coord_pair in pt_coord_list:
            plaintext += key[int(coord_pair[0])][int(coord_pair[1])]

        return plaintext

def solve(ciphertext:str, key:Iterable[Iterable[str]]) -> str:
    """
    Solves a Bifid Cipher
    Params:
        - ciphertext : Text to be decrypted
        - key : a 5x5 2D polybius table
    """
    cipher = BifidCipher(ciphertext)
    return cipher.solve(key)

if __name__ == "__main__":
    print(solve("UAEOLWRINS", [["B", "G", "W", "K", "Z"],
                               ["Q", "P", "N", "D", "S"],
                               ["I", "O", "A", "X", "E"],
                               ["F", "C", "L", "U", "M"],
                               ["T", "H", "Y", "V", "R"]]))