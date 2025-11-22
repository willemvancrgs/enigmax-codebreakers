import string

# INPUT CIPHERTEXT
ciphertext = input("Enter ciphertext: ").strip()

alphabet = list(string.ascii_uppercase)

# INPUT KEYWORD
keyword = input("Enter keyword: ").strip().upper()

seen = set()
keyword_letters = []
for ch in keyword:
    if ch in alphabet and ch not in seen:
        keyword_letters.append(ch)
        seen.add(ch)

# INPUT TOTAL MONOME COUNT
while True:
    try:
        total_monome_count = int(input("Total number of monomes (including keyword letters): ").strip())
        if total_monome_count >= len(keyword_letters) and 1 <= total_monome_count <= 9:
            break
        print(f"Enter a number between {len(keyword_letters)} and 9.")
    except ValueError:
        print("Enter a valid number.")


# BUILD MONOME LETTER LIST
monome_letters = keyword_letters.copy()

remaining_needed = total_monome_count - len(keyword_letters)
if remaining_needed > 0:
    print(f"Enter {remaining_needed} additional monome letter(s):")
while len(monome_letters) < total_monome_count:
    L = input(f"Monome letter {len(monome_letters)+1}: ").strip().upper()
    if len(L) == 1 and L in alphabet and L not in monome_letters:
        monome_letters.append(L)
    else:
        print("Invalid or duplicate letter.")

# INPUT MONOME DIGITS
monome_numbers = []
print("Enter a unique 1-digit number for each monome letter: ")

for L in monome_letters:
    while True:
        N = input(f"Digit for {L}: ").strip()
        if N.isdigit() and len(N) == 1 and N not in monome_numbers:
            monome_numbers.append(N)
            break
        print("Invalid or duplicate digit.")

# OMITTED LETTERS
print("Enter omitted letters (leave blank for none)")
omit_input = input("Omitted letters: ").strip().upper()

omitted_letters = []
for ch in omit_input:
    if ch in alphabet and ch not in omitted_letters:
        omitted_letters.append(ch)

# LETTERS NEEDING DINOMES
remaining_letters = [L for L in alphabet if L not in monome_letters and L not in omitted_letters]

print("Remaining letters needing dinomes: ")
print(remaining_letters)

# DETERMINE ROW DIGITS
all_digits = list("0123456789")
remaining_digits = [d for d in all_digits if d not in monome_numbers]

print(f"Digits available for dinome rows: {remaining_digits}")

while True:
    try:
        use_row_count = int(input(f"How many row digits will you use? (1–{len(remaining_digits)}): ").strip())
        if 1 <= use_row_count <= len(remaining_digits):
            break
        print("Enter a valid number.")
    except ValueError:
        print("Enter a valid integer.")

print("Enter the row first digits: ")

row_headers = []
for i in range(use_row_count):
    while True:
        d = input(f"Row {i+1} first-digit: ").strip()
        if d in remaining_digits and d not in row_headers:
            row_headers.append(d)
            break
        print("Invalid or duplicate row digit.")

# BUILD DINOME LIST IN EXACT ORDER
dinome_list = []
for first_digit in row_headers:
    for second_digit in monome_numbers:
        dinome_list.append(first_digit + second_digit)

if len(dinome_list) < len(remaining_letters):
    for d1 in remaining_digits:
        for d2 in all_digits:
            code = d1 + d2
            if code not in dinome_list and code not in monome_numbers:
                dinome_list.append(code)
            if len(dinome_list) >= len(remaining_letters):
                break
        if len(dinome_list) >= len(remaining_letters):
            break

dinome_list = dinome_list[:len(remaining_letters)]

# BUILD DECODE MAP
decode_map = {}

for L, N in zip(monome_letters, monome_numbers):
    decode_map[N] = L

for L, code in zip(remaining_letters, dinome_list):
    decode_map[code] = L

# DECODER
def decode(ct):
    i = 0
    out = ""
    while i < len(ct):
        if ct[i] in decode_map:
            out += decode_map[ct[i]]
            i += 1
            continue
        if i + 1 < len(ct) and ct[i:i+2] in decode_map:
            out += decode_map[ct[i:i+2]]
            i += 2
            continue
        out += "?"
        i += 1
    return out

# PRINT DECODED PLAINTEXT
print("Decoded plaintext:")
print(decode(ciphertext))
