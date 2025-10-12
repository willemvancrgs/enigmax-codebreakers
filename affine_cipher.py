#Affine Cipher
key1 = int(input("Print the first number of the key: "))
while key1 < 1 or key1 > 25:
  key1 = int(input("Invalid input. Input a valid key: "))
if key1 % 2 == 0 or key1 % 13 == 0:
  print("Cannot be decrypted")
else:
  key2 = int(input("Print the second number of the key: "))
  message = input("Input the message to be decrypted: ")
  
  def mod_inverse(a, m):
    t, new_t = 0, 1
    r, new_r = m, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if t < 0:
        t += m
    return t
  
  def solve(ciphertext, a_inv, b):
    plaintext = ""
    for char in ciphertext.upper():
        if char.isalpha():
            y = ord(char) - ord('A')
            x = (a_inv * (y - b)) % 26
            plaintext += chr(x + ord('A'))
        else:
            plaintext += char
    return plaintext
  
  inv_key1 = mod_inverse(key1, 26)
  plaintext = solve(message, inv_key1, key2)
  print(plaintext)
