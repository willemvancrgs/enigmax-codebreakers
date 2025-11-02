import math
import argparse

def encode(plain_text: str, key: str) -> str:
    """
    Encode a message using the Beaufort cipher.
    
    Args:
        plain_text (str): The text to encode
        key (str): The key to use for encoding
        
    Returns:
        str: The encoded cipher text
    
    Note:
        The Beaufort cipher is reciprocal, meaning the same process is used for both
        encoding and decoding. However, we provide separate functions for clarity.
    """
    return decode(plain_text, key)

def decode(cipher_text: str, key: str) -> str:
    """
    Decode a message using the Beaufort cipher with a known key.
    
    Args:
        cipher_text (str): The cipher text to decode
        key (str): The key to use for decoding
        
    Returns:
        str: The decoded plain text
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_text = cipher_text.replace(" ", "").lower()
    key = key.lower()
    deciphered_text = []
    key_current = 0
    key_max = len(key) - 1

    # Process each letter using Beaufort cipher algorithm
    for letter in cipher_text:
        if letter in alphabet:
            # Convert letters to numerical values (0-25)
            letter_val = ord(letter) - 97
            key_letter = key[key_current]
            key_val = ord(key_letter) - 97
            
            # Beaufort cipher formula: (key_letter - cipher_letter) mod 26
            decoded_val = (key_val - letter_val) % 26
            decoded_letter = alphabet[decoded_val]
            deciphered_text.append(decoded_letter)
            
            # Cycle through key letters
            key_current = (key_current + 1) % (key_max + 1)
            
    return ''.join(deciphered_text).upper()
def crack_cipher(cipher_text: str) -> tuple[str, str]:
    """
    Attempt to crack the Beaufort cipher without a known key using frequency analysis.
    
    Args:
        cipher_text (str): The cipher text to crack
        
    Returns:
        tuple[str, str]: A tuple containing (decoded_text, discovered_key)
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_text = cipher_text.replace(" ", "").lower()
    
    # Initial decoding attempt
    initial_decode = []
    for letter in cipher_text:
        if letter in alphabet:
            # Beaufort reciprocal property: 25 - letter_value
            letter_val = ord(letter) - 97
            decoded_val = (25 - letter_val) % 26
            initial_decode.append(alphabet[decoded_val])
    
    result = ''.join(initial_decode)
    length_of_text = len(result)
    
    # Calculate Index of Coincidence (IC)
    def calculate_ic(text: str) -> float:
        """Calculate the Index of Coincidence for a text."""
        freq = [0] * 26
        for ch in text:
            if ch.isalpha():
                freq[ord(ch) - ord('a')] += 1
        numer = sum(f * (f - 1) for f in freq)
        denom = length_of_text * (length_of_text - 1)
        return numer / denom if denom > 0 else 0

    # Estimate key length using IC
    ic = calculate_ic(result)
    est_key_length = max(1, int(round(
        ((0.0667 - 0.0385) * length_of_text) /
        (((0.0667 - ic) * (length_of_text - 1)) + (length_of_text * (ic - 0.0385)))
    )))
    
    # Split text into columns based on key length
    columns = [[] for _ in range(est_key_length)]
    for i, letter in enumerate(result):
        columns[i % est_key_length].append(letter)
    
    # Analyze each column to find key letters
    key_letters = []
    for column in columns:
        freq = [0] * 26
        for ch in column:
            if ch.isalpha():
                freq[ord(ch) - ord('a')] += 1
        
        # Find most frequent letter and calculate corresponding key letter
        most_frequent = freq.index(max(freq))
        key_val = ((most_frequent - 4) % 26)  # Assuming 'E' is most common
        key_val = (25 - key_val) % 26  # Beaufort cipher adjustment
        key_letters.append(chr(key_val + 97))
    
    discovered_key = ''.join(key_letters)
    
    # Decode using discovered key
    decoded_text = decode(cipher_text, discovered_key)
    return (decoded_text, discovered_key)

def solve(cipher_text: str, key: str = "") -> tuple[str, str]:
    """
    Solve the Beaufort cipher with the given cipher text and optional key.
    
    Args:
        cipher_text (str): The cipher text to decode (can include spaces)
        key (str, optional): The key to use for decoding. If not provided, will attempt to crack.
    
    Returns:
        tuple[str, str]: (decrypted_text, discovered_key)
    """
    if key:
        return (decode(cipher_text, key), key)
    return crack_cipher(cipher_text)

def main():
    """Command line interface for the Beaufort cipher."""
    parser = argparse.ArgumentParser(description='Encode/Decode text using the Beaufort cipher')
    parser.add_argument('action', choices=['encode', 'decode'], help='Action to perform')
    parser.add_argument('text', help='Text to process')
    parser.add_argument('--key', help='Key for encoding/decoding', default='')
    
    args = parser.parse_args()
    
    if args.action == 'encode':
        result = encode(args.text, args.key)
        print(f"Encoded text: {result}")
    else:
        result, key = solve(args.text, args.key)
        if args.key:
            print(f"Decoded text: {result}")
        else:
            print(f"Decoded text: {result}")
            print(f"Discovered key: {key}")

if __name__ == '__main__':
    main()