readable_distance = ['404','meter/s', 'cm/s', 'Km/s', 'mile/s', 'foot/s', 'inch/es']  
        
def distance_dictionary(selection_1, selection_2, value):
    match selection_1:
        case 1: 
            func = meter_dictionary(selection_2, value)
        case 2: 
            func = centimeter_dictionary(selection_2, value)
        case 3: 
            func = kilometer_dictionary(selection_2, value)
        case 4: 
            func = mile_dictionary(selection_2, value)
        case 5: 
            func = foot_dictionary(selection_2, value)
        case 6: 
            func = inch_dictionary(selection_2, value)

    print(f'{value} {readable_distance[selection_1]} converted to {readable_distance[selection_2]} is: {func:.2f} {readable_distance[selection_2]}')
    input('Enter any key to continue...')


def meter_dictionary(selection_2, value):
    conversions = {
        2: value * 100,          # to centimeter
        3: value / 1000,         # to kilometer
        4: value / 1609.344,     # to mile
        5: value * 3.28084,      # to foot
        6: value * 39.3701       # to inch
    }
    return conversions.get(selection_2, "Invalid conversion")


def centimeter_dictionary(selection_2, value):
    conversions = {
        1: value / 100,          # to meter
        3: value / 100000,       # to kilometer
        4: value / 160934.4,     # to mile
        5: value / 30.48,        # to foot
        6: value / 2.54          # to inch
    }
    return conversions.get(selection_2, "Invalid conversion")


def kilometer_dictionary(selection_2, value):
    conversions = {
        1: value * 1000,         # to meter
        2: value * 100000,       # to centimeter
        4: value / 1.609344,     # to mile
        5: value * 3280.84,      # to foot
        6: value * 39370.1       # to inch
    }
    return conversions.get(selection_2, "Invalid conversion")

        
def mile_dictionary(selection_2, value):
    conversions = {
        1: value * 1609.344,     # to meter
        2: value * 160934.4,     # to centimeter
        3: value * 1.609344,     # to kilometer
        5: value * 5280,         # to foot
        6: value * 63360         # to inch
    }
    return conversions.get(selection_2, "Invalid conversion")

        
def foot_dictionary(selection_2, value):
    conversions = {
        1: value / 3.28084,      # to meter
        2: value * 30.48,        # to centimeter
        3: value / 3280.84,      # to kilometer
        4: value / 5280,         # to mile
        6: value * 12            # to inch
    }
    return conversions.get(selection_2, "Invalid conversion")


def inch_dictionary(selection_2, value):
    conversions = {
        1: value / 39.3701,      # to meter
        2: value * 2.54,         # to centimeter
        3: value / 39370.1,      # to kilometer
        4: value / 63360,        # to mile
        5: value / 12            # to foot
    }
    return conversions.get(selection_2, "Invalid conversion")