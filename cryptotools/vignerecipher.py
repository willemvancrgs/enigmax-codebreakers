key = input("Key: ").upper()
text = input("Encrypted text: ").upper()
al = [] #answer list

klen = len(key) #key length
kcount = 0

for char in text: #making a loop for every character in the text
    if char.isalpha():  # ignoring spaces
        tv = ord(char) - ord('A') #text value
        kv = ord(key[kcount % klen]) - ord('A') #key value
        dv = (tv - kv) % 26 #making it wrap around
        al.append(chr(dv + ord('A'))) #adding the letter to answer list
        kcount += 1  # next key letter
    else:
        al.append(char)  # ignoring spaces

answer = ''.join(al)
print(answer)

#it has support for letters and spaces