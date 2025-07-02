readable_temp = ['404', 'Celsius (C)', 'Fahrenheit (F)', 'Kelvin (K)']

def temp_dictionary(selection_1, selection_2, value):
    match selection_1:
        case 1: 
            func = celsius_dictionary(selection_2, value)
        case 2: 
            func = fahrenheit_dictionary(selection_2, value)
        case 3: 
            func = kelvin_dictionary(selection_2, value)

    print(f'{value} degree/s {readable_temp(selection_1)} converted to {readable_temp(selection_2)} is: {func:.2f} degree/s {readable_temp(selection_2)}')
    input('Enter any key to continue...')


def celsius_dictionary(selection_2, value):
    conversions = {
        2: (value * 9/5) + 32,      # Celsius to Fahrenheit
        3: value + 273.15           # Celsius to Kelvin
    }
    return conversions.get(selection_2, "Invalid conversion")


def fahrenheit_dictionary(selection_2, value):
    conversions = {
        1: (value - 32) * 5/9,      # Fahrenheit to Celsius
        3: (value - 32) * 5/9 + 273.15  # Fahrenheit to Kelvin
    }
    return conversions.get(selection_2, "Invalid conversion")


def kelvin_dictionary(selection_2, value):
    conversions = {
        1: value - 273.15,               # Kelvin to Celsius
        2: (value - 273.15) * 9/5 + 32   # Kelvin to Fahrenheit
    }
    return conversions.get(selection_2, "Invalid conversion")