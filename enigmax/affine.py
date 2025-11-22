def solve(ciphertext: str, a: int | str, b: int | str) -> str:
    """
    Decrypt an Affine / Periodic Affine cipher given the ciphertext and keys.

    Args:
        ciphertext (str): The encrypted message to be decrypted.
        a (int or str): The multiplicative key. Can be:
            - int: a single key for standard Affine cipher
            - str: a string of letters for periodic Affine cipher
        b (int or str): The additive key. Can be:
            - int: a single key for standard Affine cipher
            - str: a string of letters for periodic Affine cipher

    Returns:
        str: The decrypted plaintext message.

    Raises:
        ValueError: If 'a' / charecter in 'a' has no modular inverse modulo 26
        (i.e., gcd(a, 26) != 1)
    """
    # Check if 'a' is valid for the Affine cipher (must be coprime with 26)
    if isinstance(a, str):
        a = a.upper()

        if isinstance(b, int):
            b += ord('A') - 1
            b = chr(b)

    if isinstance(b, str):
        b = b.upper()
        if isinstance(a, int):
            a += ord('A') - 1
            a = chr(a)

    if isinstance(a, int):
        if a < 1 or a > 25 or a % 2 == 0 or a % 13 == 0:
            raise ValueError(
                "Key 'a' must be coprime with 26 (not divisible by 2 or 13,\
                and 1 <= a <= 25)."
                )
        return decrypt_affine(ciphertext, a, b)  # type: ignore

    for char in a:
        char = ord(char) - ord('A') + 1
        if char < 1 or char > 25 or char % 2 == 0 or char % 13 == 0:
            raise ValueError(
                f"Letter {char} in key 'a' must be coprime with 26\
                (not divisible by 2 or 13, and 1 <= a <= 25)."
            )

    return decrypt_periodic_affine(ciphertext, a, b)  # type: ignore


def decrypt_char(char: str, a_inv: int, b: int):
    """Decrypt a single uppercase charecter using the Affine cipher"""
    if char.isalpha():
        y = ord(char) - ord('A')
        x = (a_inv * (y - b)) % 26
        return chr(x + ord('A'))
    else:
        return char


def decrypt_affine(ciphertext: str, a: int, b: int):
    """
    Decrypt a ciphertext encrypted with the Affine cipher.
    Args:
        ciphertext (str): The encrypted message to be decrypted.
        a (int): The multiplicative key used in the Affine cipher encryption.
        b (int): The 'b' value used in the Affine cipher encryption.
    Returns:
        str: The decrypted plaintext message.
    Notes:
        - Only alphabetic characters are decrypted; non-alphabetic characters
          are preserved as-is
        - The function assumes ciphertext is in English alphabet (A-Z)
    """
    a_inv = pow(a, -1, 26)
    plaintext = ""
    for char in ciphertext.upper():
        plaintext += decrypt_char(char, a_inv, b)
    return plaintext


def decrypt_periodic_affine(ciphertext: str, a_key: str, b_key: str):
    """
    Decrypt a ciphertext encrypted with Periodic Affine Cipher.
    Args:
        ciphertext (str): The encrypted message to be decrypted
        a_key (str): The string of letters acting as the multiplicative key
        b_key (str): The string of letters acting as the intercept
    Returns:
        str: The decrypted plaintext message.
    Notes:
        - Only alphabetic characters are decrypted; non-alphabetic characters
          are preserved as-is
        - The function assumes ciphertext is in English alphabet (A-Z)
        - The index of the letters of the a_key must be coprimes of 26. So the
          only usable letters are:
            A, C, E, G, I, K, O, Q, S, U, W, Y
        - Uses 1-based mapping for a_key and b_key
    """
    plaintext = ""
    for i, char in enumerate(ciphertext.upper()):
        a = ord(a_key[i % len(a_key)]) - ord('A') + 1
        a_inv = pow(a, -1, 26)
        b = ord(b_key[i % len(b_key)]) - ord('A') + 1

        plaintext += decrypt_char(char, a_inv, b)
    return plaintext


def encrypt_char(char: str, a: int, b: int) -> str:
    if char.isalpha():
        x = ord(char) - ord('A')
        y = (a*x + b) % 26
        return chr(y + ord('A'))
    else:
        return char


def encrypt_affine(plaintext: str, a: int, b: int) -> str:
    """
    Encrypt a plaintext with the Affine cipher.
    Args:
        plaintext (str): The message to be encrypted
        a (int): The slope
        b (int): The intercept
    Returns:
        str: The encrypted ciphertext
    Notes:
        - Only alphabetic characters are encrypted; non-alphabetic characters
          are preserved as-is.
        - The function assumes plaintext is in English alphabet (A-Z).
    """
    ciphertext = ""
    for char in plaintext.upper():
        ciphertext += encrypt_char(char, a, b)
    return ciphertext


def encrypt_periodic_affine(plaintext: str, a_key: str, b_key: str) -> str:
    """
    Encrypt a plaintext with Periodic Affine cipher
    Args:
        plaintext (str): The message to be encrypted
        a_key (str): The string of letters acting as the multiplicative key
        b_key (str): The string of letters acting as the intercept
    Returns:
        str: The encrypted ciphertext
    Notes:
        - Only alphabetic characters are encrypted; non-alphabetic characters
          are preserved as-is.
        - The function assumes plaintext is in English alphabet (A-Z).
        - The index of the letters of the a_key must be coprimes of 26. So the
          only usable letters are:
            A, C, E, G, I, K, O, Q, S, U, W, Y
        - Uses 1-based mapping for a_key and b_key
    """
    ciphertext = ""
    for i, char in enumerate(plaintext.upper()):
        a = ord(a_key[i % len(a_key)]) - ord('A') + 1
        b = ord(b_key[i % len(b_key)]) - ord('A') + 1
        ciphertext += encrypt_char(char, a, b)
    return ciphertext


if __name__ == "__main__":
    # Tests

    print("Affine decrypting\n")

    # HELLO
    plaintext = solve("RCLLA", 5, 8)
    print(plaintext)
    # THE QUICK BROWN FOX JUMPS OVER 13 LAZY DOGS.
    plaintext = solve("Fho muwka vbiyt din luexq ijob 13 pgrc zisq.", 15, 6)
    print(plaintext)

    print("\nAffine encrypting and decrypting\n")

    # ELCEKMJ TAEKMO!
    ciphertext = encrypt_affine("Chicken Jockey!", 17, 22)
    print(ciphertext)
    # CHICKEN JOCKEY!
    plaintext = solve(ciphertext, 17, 22)
    print(plaintext)

    print("\nPeriodic encrypting and decrypting\n")

    plaintext = solve("Fho muwka vbiyt din luexq ijob 13 pgrc zisq.", 15, "F")
    print(plaintext)

    ciphertext = encrypt_periodic_affine("I LOVE HORSES", "WOKE", "MOB")
    print(ciphertext)
    plaintext = decrypt_periodic_affine(ciphertext, "WOKE", "MOB")
    print(plaintext)
    plaintext = solve(ciphertext, "WOKE", "MOB")
    print(plaintext)
