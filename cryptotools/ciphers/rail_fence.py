def split(cipher_text: str, rail_count: int = 3) -> dict[int, str]:
    """Encode text using Rail Fence cipher."""
    rails = {i: '' for i in range(rail_count)}
    rail_num = 0
    direction = True # True for down

    for letter in cipher_text:
        rails[rail_num] += letter
        
        if direction:
            rail_num += 1
        else:
            rail_num -= 1
        
        if rail_num == rail_count-1 or rail_num == 0:
            direction = not direction
            
    return rails

def compose(rails: dict[int, str], order: list[int] | None = None) -> str:
    """Compose rails into one string"""
    if order is None:
        order = range(len(rails))
    return "".join(rails[j] for j in order)

if __name__ == "__main__":
    text = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    encoded = encode_railfence(text, 5)
    print(encoded)
    print(compose(encoded, []))