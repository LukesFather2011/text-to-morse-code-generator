# This module converts text to morse or morse to text.
from morse import Morse

morse_code_dictionary = Morse.MORSE_DICT


def text_to_morse(text):
    """converts string to text to morse code"""
    converted_string = ""

    # parses input text and assigns in the equivalent morse code.
    for letter in text:

        try:
            converted_letter = morse_code_dictionary[letter.lower()]
            converted_string += converted_letter + "   "

        except KeyError:
            continue

    return converted_string

