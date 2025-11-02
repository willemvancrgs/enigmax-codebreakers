def zigzag(offset: int, rail_count: int = 3) -> tuple[int, int]:#
        """Return the starting rail number and the direction."""
        period = 2 * (rail_count - 1)
        m = offset % period
        if m < rail_count:
            return m, 1
        else: # If the ofset makes the start go back up again
            return period - m, -1 

def encrypt(plaintext: str, rail_count: int = 3, offset: int = 0) -> dict[int, str]:
    """Encode text using Rail Fence cipher."""
    rails = {i: '' for i in range(rail_count)}
    rail_num, direction = zigzag(offset, rail_count)

    # Positive direction means the fence is going down

    for letter in plaintext:
        rails[rail_num] += letter
        
        rail_num += direction
        
        if rail_num == rail_count-1 or rail_num == 0:
            direction *= -1
            
    return rails

def compose(rails: dict[int, str], order: list[int] | None = None) -> str:
    """Compose rails into one string"""
    if order is None:
        order = list(range(len(rails)))
    return "".join(rails[j] for j in order)

def decrypt(ciphertext: str, rail_count: int = 3, offset: int = 0):
    """"""
    text_length = len(ciphertext)

    # 1: Make zigzag
    rail, direction = zigzag(offset, rail_count)

    positions: list[int] = []

    for _ in range(text_length):
        positions.append(rail)
        rail += direction
        if rail == 0 or rail == rail_count - 1:
            direction *= -1
    
    print(positions)

    # 2: Determine rail lengths
    rail_lengths = [positions.count(r) for r in range(rail_count)] # todo: improve mathematically

    # 3: Split ciphertext
    rails_list: list[list[str]] = []
    pos1 = 0
    pos2 = 0

    for count in rail_lengths:
        pos1 = pos2
        pos2 += count
        rails_list.append(list(ciphertext[pos1:pos2]))

    # 4: Create plaintext
    plaintext: list[str] = []

    for rail in positions:
        plaintext.append(rails_list[rail][0])
        rails_list[rail].pop(0)

    return "".join(plaintext)
    

if __name__ == "__main__":
    text = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    encoded = encrypt(text, 5, 7)
    print(encoded)
    print(compose(encoded, []))

    print(decrypt("HKFTECBNOQIRWXUO", 4, 5))