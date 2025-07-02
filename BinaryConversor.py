from MyFunctions import display_menu
def binary_menu():
    convert_options = ["Binary Menu!", "Convert to binary", "Convert from binary"]
    len_options = len(convert_options)

    while True:
        display_menu(convert_options)

        option = int(input(f'Please, select a category between 1 and {len_options - 1}. Enter {len_options} to exit: '))

        if option == len_options : break
        elif not 0 < option <= len_options: continue 
        #Checks if the selection is NOT between the valid options
        else: 
            if option == 1: #Convert to
                convert_to_binary()
            if option == 2: #Convert from
                convert_from_binary()


def convert_to_binary():
    
    user_input = input("Enter text or number to convert to binary: ")

    try:
        # Try converting to an integer
        number = int(user_input)
        binary = bin(number)[2:]
        print(f"The number {number} in binary is: {binary}")
    except ValueError:
        # If it's not a number, treat it as text
        binary = ' '.join(format(ord(char), '08b') for char in user_input)
        print(f'The text "{user_input}" in binary is: {binary}')
    input('Enter any key to continue...')


def convert_from_binary():
    user_input = input("Enter binary to convert, use space-separated bytes (8) for text: ")

    try:
        if ' ' in user_input.strip():  # Likely text
            chars = user_input.strip().split()
            text = ''.join(chr(int(b, 2)) for b in chars)
            print(f"The binary as text is: {text}")
        else:  # Likely a number
            number = int(user_input, 2)
            print(f"The binary as number is: {number}")
        input('Enter any key to continue...')
    except ValueError:
        print("Invalid input. Make sure to enter only 0s and 1s.")