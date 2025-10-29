import math

def solve(cipher_text_spaces, key=""):
    """
    Solve the Beaufort cipher with the given cipher text and optional key.
    
    Args:
        cipher_text_spaces (str): The cipher text to decode (can include spaces)
        key (str, optional): The key to use for decoding. If not provided, will attempt to crack.
    
    Returns:
        tuple: (decrypted_text, discovered_key) where both are strings
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_text = cipher_text_spaces.replace(" ", "").lower()
    key_letter = new_letter = result = ''
    key_guess = key
    key_current = est_key_length = 0
    key_max = len(key) - 1 if key else 0
    deciphered_text = []

    if key:
        # Decode with known key
        for letter in cipher_text:
            if letter in alphabet:
                letter = ord(letter) - 97
                key_letter = key[key_current]
                key_letter = ord(key_letter) - 97
                letter = key_letter - letter
                letter = letter % 26
                new_letter = alphabet[letter]
                deciphered_text.append(new_letter)
                key_current += 1
                if key_current > key_max:
                    key_current = 0
        result = ''.join(deciphered_text)
        return (result.upper(), key)
    else:
        # Try to crack without key
        for letter in cipher_text:
            letter = ord(letter) - 97
            letter = 25 - letter
            new_letter = alphabet[letter]
            deciphered_text.append(new_letter)
        
        result = ''.join(deciphered_text)
        length_of_text = len(result)
        x = 0
        
        # Calculate Index of Coincidence
        freq = [0] * 26
        for ch in result:
            if ch.isalpha():
                freq[ord(ch) - ord('a')] += 1
        numer_of_IC = sum(f * (f - 1) for f in freq)
        IC = (numer_of_IC)/(length_of_text*(length_of_text-1))
        est_key_length = int(round(((0.0667-0.0385)*length_of_text)/(((0.0667-IC)*(length_of_text-1)) + (length_of_text * (IC - 0.0385))),0))
        
        # Split text for analysis
        split_up_text = [[] for _ in range(est_key_length)]
        for letter in result:
            for counter in range(est_key_length):
                split_up_text[counter].append(letter)
        
        # Check IC consistency
        for row in split_up_text:
            freq = [0] * 26
            for ch in row:
                if ch.isalpha():
                    freq[ord(ch) - ord('a')] += 1
            numer_of_IC = sum(f * (f - 1) for f in freq)
            IC = numer_of_IC / (len(row) * (len(row) - 1))
            if math.isclose(IC, 0.066, rel_tol=1e-2):
                x += 1

        # Process based on IC analysis
        split_up_text = [[] for _ in range(est_key_length)]
        letter_current = 0
        for letter in result:
            split_up_text[letter_current].append(letter)
            letter_current += 1
            if letter_current == est_key_length:
                letter_current = 0

        # Calculate key
        Total_Beaufort_Key = []
        for row_number, row in enumerate(split_up_text):
            freq = [0] * 26
            for ch in row:
                if ch.isalpha():
                    freq[ord(ch) - ord('a')] += 1
            most_frequent_letter = freq.index(max(freq))
            Beaufort_key = ((most_frequent_letter - 4) % 26)
            Beaufort_key = (25 - Beaufort_key) % 26
            individual_key = chr(Beaufort_key + 97)
            Total_Beaufort_Key.append(individual_key)

        discovered_key = ''.join(Total_Beaufort_Key)
        
        # Use discovered key to decode
        key_current = 0
        key_max = len(discovered_key) - 1
        final_result_list = []
        
        for letter in cipher_text:
            if letter in alphabet:
                letter = ord(letter) - 97
                key_letter = discovered_key[key_current]
                key_letter = ord(key_letter) - 97
                letter = key_letter - letter
                letter = letter % 26
                new_letter = alphabet[letter]
                final_result_list.append(new_letter)
                key_current += 1
                if key_current > key_max:
                    key_current = 0
                    
        final_result = ''.join(final_result_list)
        return (final_result.upper(), discovered_key)