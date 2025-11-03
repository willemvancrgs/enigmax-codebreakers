from itertools import cycle #thing that allows infinetly looping until coondition is met


def solve(ciphertext: str, key_type: int, word_key: str | None = None, numeric_key: str | None = None) -> str:
    """Decipher AMSCO ciphertext.

    Parameters:
    - ciphertext: str
    - key_type: int (1 for word key, 2 for numeric key)
    - word_key: str (required if key_type==1)
    - numeric_key: str or iterable of digits (required if key_type==2)

    Returns:
    - plaintext: str
    """
    # Replicated original logic but using parameters instead of input(), and returning instead of printing.

    # Build and validate key depending on key_type
    key = None
    if key_type == 1:
        if word_key is None:
            word_key = ''
        word_key = word_key.upper()
        sorted_letters = sorted(list(word_key))
        key = [sorted_letters.index(ch) + 1 for ch in word_key]
    elif key_type == 2:
        # Allow numeric_key to be provided as string or iterable of digits
        if numeric_key is None:
            key = []
        else:
            key = [int(d) for d in str(numeric_key)]
    else:
        raise ValueError("key_type must be 1 (word) or 2 (numeric)")

    if not key:
        raise ValueError("Key must be provided and non-empty")

    #actual decipherer
    col_pattern: dict[int, list[int]] = {}
    col_letters: dict[int, list[str]] = {}
    key_cycle = cycle(key)
    size_cycle = cycle([1, 2])
    counter = 1
    x = 0

    # How many letters go into each column
    while x < len(ciphertext): 
        col_num = next(key_cycle)
        cell_size = next(size_cycle)
        
        if x + 1 == len(ciphertext):
            cell_size = 1
            
        col_pattern.setdefault(col_num, []).append(cell_size)
        
        if counter == len(key) and len(key) % 2 == 0:
            counter = 0
            next(size_cycle)
        counter += 1
        x += cell_size

    # Fill each column with letters
    text_iter = iter(ciphertext)
    for col_index in sorted(col_pattern.keys()):
        for size in col_pattern[col_index]:
            chunk = ''.join(next(text_iter) for _ in range(size))
            col_letters.setdefault(col_index, []).append(chunk)

    # Reverse columns
    for col in col_letters:
        col_letters[col].reverse()

    # Reconstruct plaintext
    key_cycle = cycle(key)
    plaintext = ''
    while len(plaintext) < len(ciphertext):
        plaintext += col_letters[next(key_cycle)].pop()

    return plaintext


if __name__ == "__main__":
    # Preserve original interactive behaviour
    ciphertext = input("Cipher text: ")
    key_type = int(input("Word key (1) or int key (2): "))

    if key_type == 1:
        word_key = input("Enter word key: ").upper()
        result = solve(ciphertext, key_type, word_key=word_key)
    elif key_type == 2:
        numeric_key = input("Input numeric key: ")
        result = solve(ciphertext, key_type, numeric_key=numeric_key)
    else:
        raise ValueError("key_type must be 1 (word) or 2 (numeric)")

    print(result)