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
    """Decrypt a ciphertext"""
    text_length = len(ciphertext)

    # 1: Determine rail lengths and their positions in the ciphertext
    cycle_len = 2 * rail_count - 2
    full_cycles = text_length // cycle_len
    remaining = text_length % cycle_len

    # 1.1: base counts from full cycles
    counts = [2 * full_cycles] * rail_count
    counts[0] = counts[-1] = full_cycles  # top and bottom rails

    # 1.2: determine which rails get letters from the remaining partial cycle
    start_rail, direction = zigzag(offset, rail_count)
    for i in range(remaining):
        rail = start_rail + i * direction
        # reflect at top/bottom rails
        if rail >= rail_count:
            rail = cycle_len - rail
        elif rail < 0:
            rail = -rail
        counts[rail] += 1

    # 1.3 Create rail positions
    rail_positions: list[int] = []
    for i in range(len(counts)):
        rail_positions.append(sum(counts[:i]))

    # 3: Create plaintext
    plaintext: list[str] = []

    rail_indices = [0] * rail_count 
    rail, direction = zigzag(offset, rail_count)

    for _ in range(text_length):
        plaintext.append(ciphertext[rail_positions[rail] + rail_indices[rail]])
        rail_indices[rail] += 1

        rail += direction
        if rail == 0 or rail == rail_count - 1:
            direction *= -1

    return "".join(plaintext)
    

if __name__ == "__main__":
    text = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    encoded = encrypt(text, 5, 7)
    print(encoded)
    print(compose(encoded, []))

    print(decrypt("EOMHGHQRWUPTEOSTUBNJSRLDIKFXOEAYCOVZ", 5, 6))