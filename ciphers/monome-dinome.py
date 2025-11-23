import string
from typing import Set

def cli() -> None:
    # INPUT CIPHERTEXT
    ciphertext = input("Enter ciphertext: ").strip()

    alphabet = list(string.ascii_uppercase)
    
    def build_keyword_letters(keyword: str, alphabet: list[str]) -> list[str]:
        seen: Set[str] = set()
        keyword_letters: list[str] = []
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
                raise ValueError("Enter a valid number.")
    
    def get_monome_letters(
        keyword_letters: list[str],
        total_monome_count: int,
        alphabet: list[str]
        )-> list[str]:
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
    
    def get_monome_digits(monome_letters: list[str]) -> list[str]:
        monome_numbers: list[str] = []
        print("Enter a unique 1-digit number for each monome letter: ")
        for L in monome_letters:
            N = None
            while not (N and N.isdigit() and len(N) == 1 and N not in monome_numbers):
                N = input(f"Digit for {L}: ").strip()
                if not (N.isdigit() and len(N) == 1 and N not in monome_numbers):
                    print("Invalid or duplicate digit.")
            monome_numbers.append(N)
        return monome_numbers
    
    def get_omitted_letters(alphabet: list[str]) -> list[str]:
        print("Enter omitted letters (leave blank for none)")
        omit_input = input("Omitted letters: ").strip().upper()
        omitted_letters = []
        for ch in omit_input:
            if ch in alphabet and ch not in omitted_letters:
                omitted_letters.append(ch)
        return omitted_letters
    
    def determine_row_headers(monome_numbers: list[str], all_digits: list[str]) -> list[str]:
        remaining_digits = [d for d in all_digits if d not in monome_numbers]
        print(f"Digits available for dinome rows: {remaining_digits}")
        
        use_row_count = None
        while not (isinstance(use_row_count, int) and 1 <= use_row_count <= len(remaining_digits)):
            try:
                use_row_count = int(input(f"How many row digits will you use? (1–{len(remaining_digits)}): "))
                if not (1 <= use_row_count <= len(remaining_digits)):
                    print("Enter a valid integer")
            except ValueError:
                raise ValueError("Enter a valid integer")
    
        print("Enter the row first digits: ")
    
        row_headers = []
        for i in range(use_row_count):
            d = None
            while not (d in remaining_digits and d not in row_headers):
                d = input(f"Row {i+1} first-digit: ").strip()
                if not (d in remaining_digits and d not in row_headers):
                    print("Invalid or duplicate row digit.")
            row_headers.append(d)
                
        return row_headers
    
    def build_dinome_list(
    row_headers: list[str],
    monome_numbers: list[str],
    remaining_digits: list[str],
    all_digits: list[str],
    needed: int
) -> list[str]:

        dinome_list = []
        for first_digit in row_headers:
            for second_digit in monome_numbers:
                if len(dinome_list) < needed:
                    dinome_list.append(first_digit + second_digit)
        d1_index = 0
        while len(dinome_list) < needed and d1_index < len(remaining_digits):
            d1 = remaining_digits[d1_index]
            d2_index = 0
            while len(dinome_list) < needed and d2_index < len(all_digits):
                d2 = all_digits[d2_index]
                code = d1 + d2
                if d2 not in monome_numbers and code not in dinome_list:
                    dinome_list.append(code)
                d2_index += 1
            d1_index += 1
    
        return dinome_list[:needed]
    
    def build_decode_map(
    monome_letters: list[str],
    monome_numbers: list[str],
    remaining_letters: list[str],
    dinome_list: list[str]
) -> dict[str, str]:
        decode_map: dict[str, str] = {}
        for L, N in zip(monome_letters, monome_numbers):
            decode_map[N] = L
        for L, code in zip(remaining_letters, dinome_list):
            decode_map[code] = L
        return decode_map
    
    def decode(ct: str, decode_map: dict[str, str]) -> str:
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
    
    # INPUT KEYWORD
    keyword = input("Enter keyword: ").strip().upper()
    keyword_letters = build_keyword_letters(keyword, alphabet)

    # INPUT TOTAL MONOME COUNT
    total_monome_count = get_total_monome_count(len(keyword_letters))

    # BUILD MONOME LETTER list
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

    # BUILD DINOME list
    dinome_list = build_dinome_list(row_headers, monome_numbers, remaining_digits, all_digits, len(remaining_letters))

    # BUILD DECODE MAP
    decode_map = build_decode_map(monome_letters, monome_numbers, remaining_letters, dinome_list)

    # PRINT DECODED PLAINTEXT
    print("Decoded plaintext:")
    print(decode(ciphertext, decode_map))


if __name__ == "__main__":
    print("\n")
    cli()
