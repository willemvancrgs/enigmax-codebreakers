def polybias_decode(cipher_text: str):
    """
    Decodes the polybias cipher
    """
    polybius_square = {"11": "A", "12": "B", "13": "C",
                       "14": "D", "15": "E", "21": "F",
                       "22": "G", "23": "H", "24": "I/J",
                       "25": "K", "31": "L", "32": "M",
                       "33": "N", "34": "O", "35": "P",
                       "41": "Q", "42": "R", "43": "S",
                       "44": "T", "45": "U", "51": "V",
                       "52": "W", "53": "X", "54": "Y",
                       "55": "Z"}
    cleaned = "".join(ch for ch in cipher_text if ch.isdigit())
    decoded_message: list[str] = []

    for counter in range(0, len(cleaned), 2):
        pair = cleaned[counter:counter+2]
        letter = polybius_square.get(pair)
        if letter is None:
            letter = ""

        decoded_message.append(letter)

    decoded = "".join(decoded_message)
    print("Decoded message:", decoded)


solve = polybias_decode

if __name__ == "__main__":
    cipher_text = input(
        "Enter Polybius cipher text (digits, spaces allowed): "
    )
    cipher_text = cipher_text.strip()
    polybias_decode(cipher_text)
