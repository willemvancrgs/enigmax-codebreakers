"""
Founded by Tudor Ciobotaru...
Improved by Frazer
"""

text_to_morse = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    
    "<HH>": "........", "&": ".-...", "'": ".----.", "@": ".--.-.",
    ")": "-.--.-", "(": "-.--.", ":": "---...", ",": "--..--",
    "=": "-...-", "!": "-.-.--", ".": ".-.-.-", "-": "-....-",
    "*": "-..-", "+": ".-.-.", "\\": ".-..-.", "?": "..--..", "/": "-..-."
}

morse_to_text = {v: k for k, v in text_to_morse.items()}

def split(morse: str, word_gap: str = " /") -> list[list[str]]:
    """Split the morse into letters grouped into words."""
    split_sentence = [word.split(" ") for word in morse.split(word_gap)]
    return split_sentence
    
def decode(morse: str, word_gap: str = " /"):
    """Decode the morse."""
    split_sentence = split(morse)
    decoded_sentence = ""
    
    for word in split_sentence:
        for letter in word:
            if letter in morse_to_text:
                decoded_sentence += morse_to_text[letter]
        decoded_sentence += " "
    
    decoded_sentence = decoded_sentence.replace("0/0", "%")
    
    return decoded_sentence
 
def encode(text: str):
    """Encode text to morse."""
    text = text.replace("%","0/0")
    
    text = text.upper()
    split_text = text.split(" ")
    
    morse = ""
    for word in split_text:
        morse += " ".join([text_to_morse[letter] for letter in word]) + " / "
    
    return morse[:-3]

def cli() -> None:
    """Provide basic CLI for decoding and encoding in morse code."""
    escape = False
    while not escape:
        choice = input("Decode, encode or quit? D / E / Q: ").upper()
        match choice:
            case "D":
                morse = input("Input morse code:\n")
                print(decode(morse)+"\n")
            case "E":
                text = input("Input standard text:\n")
                print(encode(text)+"\n")
            case "Q":
                escape = True
            case _:
                print("Invalid input!\n")

if __name__ == "__main__":
    # Test Code
    cipher = ".. / .-.. --- ...- . / - .... . / -. .- - .. --- -. .- .-.. / -.-. .. .--. .... . .-. / -.-. .... .- .-.. .-.. . -. --. . / ..--- ----- ..--- ..... -.-.--"
    text = "the quick BROWN fox jumps over THE laZy dog!! 0123456789 %!.*"
    print(split(cipher))
    print(decode(cipher))
    print(encode(text))
    
    # CLI
    print("\n")
    cli()