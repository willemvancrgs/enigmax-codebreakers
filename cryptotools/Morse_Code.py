#Made by Tudor Ciobotaru

def solve(ciphertext):
    decode(ciphertext)

dictionary = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-", ".--","-..-","-.--","--..","-----",".----","..---","...--","....-",".....","-....","--...","---..","----."]
Alphabet_and_numbers = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
punctuation_morse = ["........",".-...",".----.",".--.-.","-.--.-","-.--.","---...","--..--","-...-","-.-.--",".-.-.-","-....-","-..-",".-.-.",".-..-.","..--..","-..-."]
punctuation = ["<HH>", "&", "'", "@", ")", "(", ":", ",", "=", "!", ".", "-", "*", "+", "\\", "?", "/"]
decoded = False
encoded = False
def decode(morse):
    encodedWords = morse.split("/")
    encodedSentence = []
    for each in encodedWords:
        encodedSentence.append(each.split(" "))
    decodedSentence = []
    for word in encodedSentence:
        for letter in word:
            if letter in dictionary:
                decodedSentence.append(Alphabet_and_numbers[dictionary.index(letter)])
            elif letter in punctuation_morse:
                decodedSentence.append(punctuation[punctuation_morse.index(letter)])
        decodedSentence.append(" ")
    decodedSentenceOriginal = "".join(decodedSentence)
    decodedSentenceVer2 = decodedSentenceOriginal.replace("0/0","%")
    #decoded = True
    #print(decodedSentenceOriginal)
    return (decodedSentenceVer2)
 
def encode(english):
    if "%" in english:
        english.replace("%","0/0")
    finalSentence = []
    originalSentence = english.upper()
    originalSentence = originalSentence.split(" ")
    for word in originalSentence:
        letters = [char for char in word.strip()]
        finalSentence.append(letters)
    encodedSentence = []
    for word in finalSentence:
        for letter in word:
            if letter in Alphabet_and_numbers:
                encodedSentence.append(dictionary[Alphabet_and_numbers.index(letter)])
            elif letter in punctuation_morse:
                encodedSentence.append(punctuation_morse[punctuation.index(letter)])
            encodedSentence.append(" ")
        encodedSentence.append("/")
    return ("".join(encodedSentence))

if __name__ == "__main__":
    while decoded == False and encoded == False:
        decodeOrEncode = input("Decode or Encode?\n").lower()
        if decodeOrEncode == "decode":
            decode(input())
            Continue = input("Continue? (y/n)")
            if Continue == "n" or Continue == "no":
                decoded = True
            elif Continue == "y" or Continue == "yes":
                decoded = False
        elif decodeOrEncode == "encode":
            encode(input())
            Continue = input("Continue? (y/n)")
            if Continue == "n" or Continue == "no":
                encoded = True        
            elif Continue == "y" or Continue == "yes":
                encoded = False