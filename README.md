# Enigmax Codebreakers

A collection of Python scripts to expedite solving ciphers, developed for the National Cipher Challenge 2025.

## Features

- Modular design: each cipher has its own Python module.
- Consistent interface: each module contains a `solve()` function.
- PEP8-compliant code, optionally Flake8-aligned.
- Pytest coverage for all completed ciphers.

## Setup

1. Clone the repository:  
   `git clone http://github.com/willemvancrgs/enigmax-codebreakers`  
   `cd enigmax-codebreakers`  
2. Install dependencies:  
   `pip install -r requirements.txt`  

## Usage

Each cipher module exposes a `solve()` function that takes the ciphertext and any required additional parameters. Example:

```python
from ciphers.affine import solve

ciphertext = "GIEWIV GMTLIV HIQS"
plaintext = solve(ciphertext, 5, 8)
print(plaintext)
```

## Ciphers Implemented
- Affine cipher
- Amasco cipher
- Baconian cipher
- Beaufort cipher
- Monoalphabetic cipher
- Polybias cipher
- Rail fence / Redefence cipher

## Contribution guideline
- Scripts should be in Python unless otherwise decided
- Work on changes in a seperate branch before merging
- Ensure each cipher is:
    1. [PEP8-compliant](https://peps.python.org/pep-0008/)
    2. Includes pytests
    3. Implements the base cipher class
    4. Has decode and CLI functions
    5. Optionally Flake8-aligned

## Planned Ciphers / Roadmap

1. Fix file structure
2. Make autosolvers for all existing ciphers
3. Full CLI
4. More ciphers

## Curent assignees

- Sam | Playfair cipher and double playfair
- Daniel | Vertical two square
- Samarth | Horizontal two square
- Frazer | ADFGVX cipher
- Leo | Nihilist substitution cipher
- Willem | Bifid cipher 
- Tejas | Trifid cipher
- Ibrahim | Four squares cipher