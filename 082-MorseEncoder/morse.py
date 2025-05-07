"""
Requirements:
You will use what you've learnt to create a text-based (command line) program
that takes any String input and converts it into Morse Code.
"""
from data import MORSE_CODE


def encode(plaintext: str) -> str:
    """Encode plain text to Morse code"""

    return ''.join([MORSE_CODE[char.upper()] for char in plaintext])


# Main ------------------------------------------------------------------------


if __name__ == '__main__':

    plain = input('Please enter a string to encode: ')
    try:
        encoded = encode(plain)
        print(f"In Morse, that is: {encoded}")
    except KeyError as ex:
        print(f"Sadly, {ex} cannot currently be encoded")
