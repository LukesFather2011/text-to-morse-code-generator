# This program takes user input and converts it into Morse code and vice versa.
# TODO 1: Create functions to convert text to morse, and morse to text.


# This is the welcome statement presented to the user upon running the program.
print("Hello, welcome to text-to-morse code converter")

# This loop determines if the user wants to run the program again. If False, it terminates.
again = True
while again:

    user_text = input("Please enter what you would like to convert:\n")
    morse_code_conversion = ""
    for i in user_text:
        morse_code_conversion += i
    print(morse_code_conversion)
