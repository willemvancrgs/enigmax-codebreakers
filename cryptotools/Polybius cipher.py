def polybius_decode(cipher_text):
    polybius_square = {"11": "A", "12": "B", "13": "C", "14": "D", "15": "E","21": "F", "22": "G", "23": "H", "24": "I/J", "25": "K","31": "L", "32": "M", "33": "N", "34": "O", "35": "P","41": "Q", "42": "R", "43": "S", "44": "T", "45": "U","51": "V", "52": "W", "53": "X", "54": "Y", "55": "Z"}
    cleaned = "".join(ch for ch in cipher_text if ch.isdigit())
    decoded_message = []
    for counter in range(0, len(cleaned), 2):
        pair = cleaned[counter:counter+2]
        letter = polybius_square.get(pair) 
        decoded_message.append(letter)
    decoded = "".join(decoded_message)
    print("Decoded message:", decoded)

cipher_text = input("Enter Polybius cipher text (digits, spaces allowed): ").strip()
polybius_decode(cipher_text)
