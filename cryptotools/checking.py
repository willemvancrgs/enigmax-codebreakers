import math
import numpy as np
from string import ascii_uppercase
from typing import Iterable

def consecutive_freq(text: str, length: int=4) -> dict[str: int]:
    chunk_freq = {}
    
    for i in range(len(text) - length + 1):
        chunk = text[i:i+length]
        if chunk in chunk_freq:
            chunk_freq[chunk] += 1
        else:
            chunk_freq[chunk] = 1 # Creates chunk val

    chunk_freq = dict(sorted(chunk_freq.items(), key=lambda x: x[1], reverse=True)) # returns sorted list
    return chunk_freq

def letter_freq_vector(text: str) -> list[tuple[str, float]]: # For 26-degree vector angle
    text = text.upper()
    
    total = 0
    freq = {letter: 0 for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    
    for l in text:
        if l.isalpha():
            total += 1
            freq[l] += 1

    return [(k, v/total) for k, v in freq.items()]

def shan_entropy(text: str) -> float:
    probs = letter_freq_vector(text)
    return -sum(p * math.log2(p) for p in probs)

def cosine_angle(vector1: list[float], vector2: list[float]) -> str:
    dot = sum(a*b for a,b in zip(vector1, vector2)) # Dot product of both vectors
    
    norm1 = math.sqrt(sum(a*a for a in vector1)) # Length of first vector arrow using pythag
    norm2 = math.sqrt(sum(b*b for b in vector2)) # Length of second vector arrow using pythag
    
    angle_cosine = dot / (norm1 * norm2) # Cosine ratio of the vector's aligments
    angle_cosine = max(-1, min(1, angle_cosine)) # Prevent floating point error crashes	
    angle_radians = math.acos(angle_cosine) # Angle in radians
    angle_degrees = math.degrees(angle_radians) # Angle in degrees
    
    return angle_degrees

def display_freq(freqs) -> None:
    for i in freqs:
        print(i, freqs[i])

if __name__ == "__main__":
    # Testing
    
    text = "I WISH I WISH WISH IS"

    text = text.replace(' ', '')

    display_freq(consecutive_freq(text, 4)) # Tetragram 
    print("\n") 
    print(shan_entropy(text),
          shan_entropy("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
          shan_entropy("AAAAAQAAAQAAA"), sep='\n')
    
    print(letter_freq_vector(text))

def chisq(text:str, expected:dict):
    """
    Performs the chi-squared heuristic 
    """
    value = 0
    alphabet = ascii_uppercase
    cleantext = text.upper().replace(" ", "")
    for letter in alphabet:
        nominalvalue = (expected[letter]/100)*len(cleantext)
        value += ((cleantext.count(letter) - nominalvalue) ** 2)/(nominalvalue)
    return [text, value]

def chisqrank(solutions:Iterable, expected=None):
    """
    Ranks proposed solutions with the chi-squared heursitic
    """
    ranking = []
    if expected is None:
        expected = {'E' : 12.0,'T' : 9.10,'A' : 8.12,'O' : 7.68,'I' : 7.31,'N' : 6.95,'S' : 6.28,'R' : 6.02,'H' : 5.92,'D' : 4.32,'L' : 3.98,'U' : 2.88,'C': 2.71,'M' : 2.61,'F' : 2.30,'Y' : 2.11,'W' : 2.09,'G' : 2.03,'P' : 1.82,'B' : 1.49,'V' : 1.11,'K' : 0.69,'X' : 0.17,'Q' : 0.11,'J' : 0.10,'Z' : 0.07 }
    for solution in solutions:
        ranking.append(chisq(solution, expected))
    ranking = sorted(ranking, key=lambda x: x[1])
    return ranking
