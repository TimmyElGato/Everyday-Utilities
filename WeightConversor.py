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

    print(f'{value} {readable_weight[selection_1]} converted to {readable_weight[selection_2]} is: {func:.2f}  {readable_weight[selection_2]}')

def grams_dictionary(selection_2, value):
    conversions = {
        2: value / 1000,         # Kilogram
        3: value * 1000,         # Milligram
        4: value / 453.59237,    # Pound
        5: value / 28.3495       # Ounce
    }

    return conversions.get(selection_2, "Invalid conversion")


def kilograms_dictionary(selection_2, value):
    conversions = {
        1: value * 1000,         # Gram
        3: value * 1_000_000,    # Milligram
        4: value * 2.20462,      # Pound
        5: value * 35.274        # Ounce
    }

    return conversions.get(selection_2, "Invalid conversion")


def milligrams_dictionary(selection_2, value):
    conversions = {
        1: value / 1000,         # Gram
        2: value / 1_000_000,    # Kilogram
        4: value / 453592.37,    # Pound
        5: value / 28349.5       # Ounce
    }

    return conversions.get(selection_2, "Invalid conversion")


def pounds_dictionary(selection_2, value):
    conversions = {
        1: value * 453.59237,    # Gram
        2: value / 2.20462,      # Kilogram
        3: value * 453592.37,    # Milligram
        5: value * 16            # Ounce
    }

    return conversions.get(selection_2, "Invalid conversion")


def ounces_dictionary(selection_2, value):
    conversions = {
        1: value * 28.3495,      # Gram
        2: value / 35.274,       # Kilogram
        3: value * 28349.5,      # Milligram
        4: value / 16            # Pound
    }

    return conversions.get(selection_2, "Invalid conversion")



