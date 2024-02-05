# This program takes user input and converts it into Morse code and vice versa.
from convert import text_to_morse

# This is the welcome statement presented to the user upon running the program.
print("Hello, welcome to text-to-morse code converter")

# This loop determines if the user wants to run the program again. If False, it terminates.
again = True
while again:

    user_text = input("Please enter what you would like to convert:\n")
    print(text_to_morse(user_text))

    print("\n")
    if input("Would you like to convert more text? y or n: ").lower() == 'n':
        again = False
