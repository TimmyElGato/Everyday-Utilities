readable_weight = ['404', 'Gram/s (g)', 'Kilogram/s (kg)', 'Milligram/s (mg)', 'Pound/s (lb)', 'Ounces (Oz)']


def weight_dictionary(selection_1, selection_2, value):
    Message(value, selection_1, selection_2)
    input('Enter any key to continue...')

def Message(value, selection_1, selection_2):
    func = 0
    match selection_1:
        case 1: 
            func = grams_dictionary(selection_2, value)
        case 2: 
            func = kilograms_dictionary(selection_2, value)
        case 3: 
            func = milligrams_dictionary(selection_2, value)
        case 4: 
            func = pounds_dictionary(selection_2, value)
        case 5: 
            func = ounces_dictionary(selection_2, value)

    print(f'{value} degree/s {readable_weight[selection_1]} converted to {readable_weight[selection_2]} is: {func:.2f} degree/s {readable_weight[selection_2]}')

def grams_dictionary(selection_2, value):
    match selection_2:
        case 2:  # Kilogram
            return value / 1000
        case 3:  # Milligram
            return value * 1000
        case 4:  # Pound
            return value / 453.59237
        case 5:  # Ounce
            return value / 28.3495

def kilograms_dictionary(selection_2, value):
    match selection_2:
        case 1:  # Gram
            return value * 1000
        case 3:  # Milligram
            return value * 1_000_000
        case 4:  # Pound
            return value * 2.20462
        case 5:  # Ounce
            return value * 35.274

def milligrams_dictionary(selection_2, value):
    match selection_2:
        case 1:  # Gram
            return value / 1000
        case 2:  # Kilogram
            return value / 1_000_000
        case 4:  # Pound
            return value / 453592.37
        case 5:  # Ounce
            return value / 28349.5

def pounds_dictionary(selection_2, value):
    match selection_2:
        case 1:  # Gram
            return value * 453.59237
        case 2:  # Kilogram
            return value / 2.20462
        case 3:  # Milligram
            return value * 453592.37
        case 5:  # Ounce
            return value * 16

def ounces_dictionary(selection_2, value):
    match selection_2:
        case 1:  # Gram
            return value * 28.3495
        case 2:  # Kilogram
            return value / 35.274
        case 3:  # Milligram
            return value * 28349.5
        case 4:  # Pound
            return value / 16



