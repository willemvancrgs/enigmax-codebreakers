import string
from typing import List, Dict

def build_keyword_letters(keyword: str, alphabet: List[str]) -> List[str]:
    seen = set()
    keyword_letters = []
    for ch in keyword:
        if ch in alphabet and ch not in seen:
            keyword_letters.append(ch)
            seen.add(ch)
    return keyword_letters


def get_total_monome_count(minimum: int) -> int:
    while True:
        try:
            total_monome_count = int(
                input("Total number of monomes (including keyword letters): ").strip()
            )
            if total_monome_count >= minimum and 1 <= total_monome_count <= 9:
                return total_monome_count
            print(f"Enter a number between {minimum} and 9.")
        except ValueError:
            print("Enter a valid number.")


def get_monome_letters(keyword_letters: List[str], total_monome_count: int, alphabet: List[str]) -> List[str]:
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
    return monome_letters


def get_monome_digits(monome_letters: List[str]) -> List[str]:
    monome_numbers = []
    print("Enter a unique 1-digit number for each monome letter: ")
    for L in monome_letters:
        while True:
            N = input(f"Digit for {L}: ").strip()
            if N.isdigit() and len(N) == 1 and N not in monome_numbers:
                monome_numbers.append(N)
                break
            print("Invalid or duplicate digit.")
    return monome_numbers


def get_omitted_letters(alphabet: List[str]) -> List[str]:
    print("Enter omitted letters (leave blank for none)")
    omit_input = input("Omitted letters: ").strip().upper()
    omitted_letters = []
    for ch in omit_input:
        if ch in alphabet and ch not in omitted_letters:
            omitted_letters.append(ch)
    return omitted_letters


def determine_row_headers(monome_numbers: List[str], all_digits: List[str]) -> List[str]:
    remaining_digits = [d for d in all_digits if d not in monome_numbers]
    print(f"Digits available for dinome rows: {remaining_digits}")

    while True:
        try:
            use_row_count = int(
                input(f"How many row digits will you use? (1–{len(remaining_digits)}): ").strip()
            )
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
    return row_headers


def build_dinome_list(row_headers: List[str], monome_numbers: List[str], remaining_digits: List[str], all_digits: List[str], needed: int) -> List[str]:

    dinome_list = []
    for first_digit in row_headers:
        for second_digit in monome_numbers:
            dinome_list.append(first_digit + second_digit)

    if len(dinome_list) < needed:
        for d1 in remaining_digits:
            for d2 in all_digits:
                code = d1 + d2
                if code not in dinome_list and d2 not in monome_numbers:
                    dinome_list.append(code)
                if len(dinome_list) >= needed:
                    break
            if len(dinome_list) >= needed:
                break

    return dinome_list[:needed]

def build_decode_map(monome_letters: List[str], monome_numbers: List[str], remaining_letters: List[str], dinome_list: List[str]) -> Dict[str, str]:
    decode_map: Dict[str, str] = {}
    for L, N in zip(monome_letters, monome_numbers):
        decode_map[N] = L
    for L, code in zip(remaining_letters, dinome_list):
        decode_map[code] = L
    return decode_map


def decode(ct: str, decode_map: Dict[str, str]) -> str:
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


def cli() -> None:
    # INPUT CIPHERTEXT
    ciphertext = input("Enter ciphertext: ").strip()

    alphabet = list(string.ascii_uppercase)

    # INPUT KEYWORD
    keyword = input("Enter keyword: ").strip().upper()
    keyword_letters = build_keyword_letters(keyword, alphabet)

    # INPUT TOTAL MONOME COUNT
    total_monome_count = get_total_monome_count(len(keyword_letters))

    # BUILD MONOME LETTER LIST
    monome_letters = get_monome_letters(keyword_letters, total_monome_count, alphabet)

    # INPUT MONOME DIGITS
    monome_numbers = get_monome_digits(monome_letters)

    # OMITTED LETTERS
    omitted_letters = get_omitted_letters(alphabet)

    # LETTERS NEEDING DINOMES
    remaining_letters = [L for L in alphabet if L not in monome_letters and L not in omitted_letters]

    print("Remaining letters needing dinomes: ")
    print(remaining_letters)

    # DETERMINE ROW DIGITS
    all_digits = list("0123456789")
    remaining_digits = [d for d in all_digits if d not in monome_numbers]

    row_headers = determine_row_headers(monome_numbers, all_digits)

    # BUILD DINOME LIST
    dinome_list = build_dinome_list(row_headers, monome_numbers, remaining_digits, all_digits, len(remaining_letters))

    # BUILD DECODE MAP
    decode_map = build_decode_map(monome_letters, monome_numbers, remaining_letters, dinome_list)

    # PRINT DECODED PLAINTEXT
    print("Decoded plaintext:")
    print(decode(ciphertext, decode_map))


if __name__ == "__main__":
    print("\n")
    cli()
