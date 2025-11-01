def solve(ciphertext: str, a: int, b: int) -> str:
  """
  Decrypts an Affine cipher given the ciphertext and keys.

  Args:
    ciphertext (str): The encrypted message to be decrypted.
    a (int): The multiplicative key used in the Affine cipher encryption.
    b (int): The additive key used in the Affine cipher encryption.

  Returns:
    str: The decrypted plaintext message.

  Raises:
    ValueError: If 'a' has no modular inverse modulo 26 (i.e., gcd(a, 26) != 1).
  """
  # Check if 'a' is valid for the Affine cipher (must be coprime with 26)
  if a < 1 or a > 25 or a % 2 == 0 or a % 13 == 0:
    raise ValueError("Key 'a' must be coprime with 26 (not divisible by 2 or 13, and 1 <= a <= 25).")
  a_inv = pow(a, -1, 26)
  return decrypt(ciphertext, a_inv, b)

def decrypt(ciphertext: str, a_inv: int, b: int):
  """
  Decrypts a ciphertext encrypted with the Affine cipher.
  Args:
    ciphertext (str): The encrypted message to be decrypted.
    a_inv (int): The modular multiplicative inverse of 'a' used in the Affine cipher encryption.
    b (int): The 'b' value used in the Affine cipher encryption.
  Returns:
    str: The decrypted plaintext message.
  Notes:
    - Only alphabetic characters are decrypted; non-alphabetic characters are preserved as-is.
    - The function assumes ciphertext is in English alphabet (A-Z).
  """

  plaintext = ""
  for char in ciphertext.upper():
      if char.isalpha():
          y = ord(char) - ord('A')
          x = (a_inv * (y - b)) % 26
          plaintext += chr(x + ord('A'))
      else:
          plaintext += char
  return plaintext

