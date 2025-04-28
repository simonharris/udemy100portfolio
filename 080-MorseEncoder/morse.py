"""
Requirements:
You will use what you've learnt to create a text-based (command line) program 
that takes any String input and converts it into Morse Code.
"""
from data import MORSE_CODE

def encode(input: str) -> str:
    

    output = [MORSE_CODE[char.upper()] for char in input]

    return ''.join(output)



