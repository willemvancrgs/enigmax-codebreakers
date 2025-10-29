from itertools import cycle #thing that allows infinetly looping until coondition is met

ciphertext = input("Cipher text: ")
key_type = int(input("Word key (1) or int key (2): "))

if key_type == 1:
    word_key = input("Enter word key: ").upper()
    sorted_letters = sorted(list(word_key))
    key = [sorted_letters.index(ch) + 1 for ch in word_key] 
elif key_type == 2:
    key = [int(d) for d in input("Input numeric key: ")]

#actual decipherer
col_pattern = {}
col_letters = {}
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
        chunk = ''.join(next(text_iter) for count in range(size))
        col_letters.setdefault(col_index, []).append(chunk)

# Reverse columns
for col in col_letters:
    col_letters[col].reverse()

# Reconstruct plaintext
key_cycle = cycle(key)
plaintext = ''
while len(plaintext) < len(ciphertext):
    plaintext += col_letters[next(key_cycle)].pop()

print(plaintext)