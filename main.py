# This program takes user input and converts it into Morse code and vice versa.
from convert import text_to_morse


def main_loop():
    """Runs the main loop of the program."""
    # Variable to manage the while loop.
    run_again = True

    while run_again:
        text_to_convert = input("Please enter the text you would like to convert:\n")
        # Refer to convert.py. Pulls morse characters from morse.py
        print(text_to_morse(text_to_convert))

        def loop_again():
            # runs main.loop again if "y", terminates if "n", and runs the inquiry again if not a valid character.
            answer = input("Would you like to convert another string? y or n:").lower()
            if answer == "y":
                main_loop()
            elif answer == "n":
                print("Have a great day! Bye!")
                return False
            else:
                print("Please enter a valid response.")
                loop_again()

        run_again = loop_again()


# This is the welcome statement presented to the user upon running the program, followed by the main.loop.
print("Hello, welcome to text-to-morse code converter")
main_loop()


