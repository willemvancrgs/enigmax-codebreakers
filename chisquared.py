from string import ascii_uppercase
from typing import Iterable

# Predicts likely solutions
# Use by running "import chisquared", and then either pass the list of solutions into chisqrank() or individually calculate the value of a solution through chisq()

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