import math
from collections import Counter
import numpy as np

def consecutive_freq(text: str, length: int=4) -> dict:
    chunk_freq = {}
    
    for i in range(len(text) - length + 1):
        chunk = text[i:i+length]
        if chunk in chunk_freq:
            chunk_freq[chunk] += 1
        else:
            chunk_freq[chunk] = 1 # Creates chunk val

    chunk_freq = dict(sorted(chunk_freq.items(), key=lambda x: x[1], reverse=True)) # returns sorted list
    return chunk_freq

def letter_freq_vector(str: text) -> list[tuple(str, float)]: # For 26-degree vector angle
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
