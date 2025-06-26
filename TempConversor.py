readable_temp = ['404', 'Celsius (C)', 'Fahrenheit (F)', 'Kelvin (K)']

def temp_dictionary(selection_1, selection_2, value):
    Message(value, selection_1, selection_2)
    input('Enter any key to continue...')

def Message(value, selection_1, selection_2):
    match selection_1:
        case 1: 
            func = celsius_dictionary(selection_2, value)
        case 2: 
            func = fahrenheit_dictionary(selection_2, value)
        case 3: 
            func = kelvin_dictionary(selection_2, value)

    print(f'{value} degree/s {readable_temp(selection_1)} converted to {readable_temp(selection_2)} is: {func:.2f} degree/s {readable_temp(selection_2)}')

def celsius_dictionary(selection_2, value):
    match selection_2:
        case 2: #Fahrenheit
            return (value * 9/5) + 32
        case 3: #Kelvin
            return value + 273.15

def fahrenheit_dictionary(selection_2, value):
    match selection_2:
        case 1: #Celsius
            return (value - 32) * (5/9)
        case 3: #Kelvin
            return (value - 32) * (5/9) + 273.15

def kelvin_dictionary(selection_2, value):
    match selection_2:
        case 1: #Celsius
            return value - 273
        case 2: #Fahrenheit
            return (value - 273.15) * (9/5) + 32

if __name__ == '__main__':
    print(readable_temp[1])