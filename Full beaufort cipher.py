import math

#variable definitions
global alphabet, result, length_of_text, le, est_key_length, key_guess
alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher_text_spaces = input("Cipher text: ")
cipher_text = cipher_text_spaces.replace(" ","").lower()
key = input("Key: ")
key_letter = new_letter = result = ''
key_guess = key
key_current = le = est_key_length = 0
key_max = len(key) - 1
deciphered_text=[]
already_tried = []
if key:
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
    for word in deciphered_text:
        result += word
    print(result.upper())
else:
    for letter in cipher_text:
        letter = ord(letter) - 97
        letter = 25 - letter
        new_letter = alphabet[letter]
        deciphered_text.append(new_letter)
    for word in deciphered_text:
        result += word
    length_of_text = len(result)
    x = 0
    est_key_length = 0
    freq = [0] * 26
    for ch in result:
        if ch.isalpha():
            freq[ord(ch) - ord('a')] += 1
    numer_of_IC = sum(f * (f - 1) for f in freq)
    IC = (numer_of_IC)/(length_of_text*(length_of_text-1))
    est_key_length = int(round(((0.0667-0.0385)*length_of_text)/(((0.0667-IC)*(length_of_text-1)) + (length_of_text * (IC - 0.0385))),0))
    split_up_text = []
    new_length = est_key_length
    while new_length > 0:
        new_length = new_length - 1
        split_up_text.append([])
    for letter in result:
        for counter in range(est_key_length):
            split_up_text[counter].append(letter)
    for row in split_up_text:
        freq = [0] * 26
        for ch in row:
            if ch.isalpha():
                freq[ord(ch) - ord('a')] += 1
        numer_of_IC = sum(f * (f - 1) for f in freq)
        IC = numer_of_IC / (len(row) * (len(row) - 1))
        if math.isclose(IC, 0.066, rel_tol=1e-2):
            x += 1
    if x >= est_key_length * 0.5:
        split_up_text = []
        Total_Beaufort_Key = []
        Beaufort_key = 0
        freq = [0] * 26
        new_length = est_key_length
        while new_length > 0:
            new_length = new_length - 1
            split_up_text.append([])
        letter_current = 0
        for letter in result:
            split_up_text[letter_current].append(letter)
            letter_current += 1
            if letter_current == est_key_length:
                letter_current = 0
        row_number = 0
        for row in split_up_text:
            for ch in row:
                if ch.isalpha():
                    freq[ord(ch) - ord('a')] += 1
            most_frequent_letter = freq.index(max(freq))
            split_up_text[row_number].append(most_frequent_letter)
            Beaufort_key = ((most_frequent_letter - 4) % 26)
            Beaufort_key = (25 - Beaufort_key) % 26
            split_up_text[row_number].append(Beaufort_key)
            row_number += 1
            if row_number == len(split_up_text):
                row_number = 0
        row_number = 0
        individual_key = ''
        for row in split_up_text:
            individual_key = split_up_text[row_number][-1]
            individual_key = chr(individual_key + 95)
            Total_Beaufort_Key.append(individual_key)
            row_number += 1
            if row_number == len(split_up_text):
                row_number = 0
        key_guess = ""
        for word in Total_Beaufort_Key:
            key_guess += word
        final_result_list = []
        final_result = ""
        for letter in cipher_text:
            if letter in alphabet:
                letter = ord(letter) - 97
                key_letter = key[key_current]
                key_letter = ord(key_letter) - 97
                letter = key_letter - letter
                letter = letter % 26
                new_letter = alphabet[letter]
                final_result_list.append(new_letter)
                key_current += 1
                if key_current > key_max:
                    key_current = 0
        for word in final_result_list:
            final_result += word
        print(final_result.upper())
    else:
        print(f"No consistent IC found. Estimated key length: {est_key_length}")
        split_up_text = []
        Total_Beaufort_Key = []
        Beaufort_key = 0
        freq = [0] * 26
        new_length = est_key_length
        while new_length > 0:
            new_length = new_length - 1
            split_up_text.append([])
        letter_current = 0
        for letter in result:
            split_up_text[letter_current].append(letter)
            letter_current += 1
            if letter_current == est_key_length:
                letter_current = 0
        row_number = 0
        for row in split_up_text:
            for ch in row:
                if ch.isalpha():
                    freq[ord(ch) - ord('a')] += 1
            most_frequent_letter = freq.index(max(freq))
            split_up_text[row_number].append(most_frequent_letter)
            Beaufort_key = ((most_frequent_letter - 4) % 26)
            Beaufort_key = (25 - Beaufort_key) % 26
            split_up_text[row_number].append(Beaufort_key)
            row_number += 1
            if row_number == len(split_up_text):
                row_number = 0
        row_number = 0
        individual_key = ''
        for row in split_up_text:
            individual_key = split_up_text[row_number][-1]
            individual_key = chr(individual_key + 95)
            Total_Beaufort_Key.append(individual_key)
            row_number += 1
            if row_number == len(split_up_text):
                row_number = 0
        key = ""
        for word in Total_Beaufort_Key:
            key += word
        final_result_list = []
        final_result = ""
        for letter in cipher_text:
            if letter in alphabet:
                letter = ord(letter) - 97
                key_letter = key[key_current]
                key_letter = ord(key_letter) - 97
                letter = key_letter - letter
                letter = letter % 26
                new_letter = alphabet[letter]
                final_result_list.append(new_letter)
                key_current += 1
                if key_current > key_max:
                    key_current = 0
        for word in final_result_list:
            final_result += word
        print(final_result.upper())
        