def encrypt(cipher_text: str, rail_count: int = 3, offset: int = 0) -> dict[int, str]:
    """Encode text using Rail Fence cipher."""
    
    def zigzag(offset: int, raiL_count: int = 3) -> tuple[int, bool]:#
        """Return the starting rail number and the direction."""
        period = 2 * (rail_count - 1)
        m = offset % period
        if m < rail_count:
            return m, True
        else: # If the ofset makes the start go back up again
            return period - m, False 

    rails = {i: '' for i in range(rail_count)}
    rail_num, direction = zigzag(offset, rail_count)

    # True direction means the fence is going down

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
        order = list(range(len(rails)))
    return "".join(rails[j] for j in order)

if __name__ == "__main__":
    text = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    encoded = encrypt(text, 5, 7)
    print(encoded)
    print(compose(encoded, []))