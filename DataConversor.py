readable_data = ['404', 'Bit/s', 'Byte/s', 'Kilobyte/s (KB)', 'Megabyte/s (MB)', 'Gigabyte/s (GB)', 'Terabyte/s (TB)']

def data_dictionary(selection_1, selection_2, value): 
    match selection_1:
        case 1:
            func = bit_dictionary(selection_2, value)
        case 2:
            func = byte_dictionary(selection_2, value)
        case 3:
            func = kilobyte_dictionary(selection_2, value)
        case 4:
            func = megabyte_dictionary(selection_2, value)
        case 5:
            func = gigabyte_dictionary(selection_2, value)
        case 6:
            func = terabyte_dictionary(selection_2, value)

    print(f'{value} degree/s {readable_data(selection_1)} converted to {readable_data(selection_2)} is: {func} degree/s {readable_data(selection_2)}')
    input('Enter any key to continue...')

    
def bit_dictionary(selection_2, value):
    # Conversion rates from 1 bit to other units
    factors = {
        2: 1 / 8,                  # Bit to Byte
        3: 1 / (8 * 1_000),        # Bit to Kilobyte
        4: 1 / (8 * 1_000_000),    # Bit to Megabyte
        5: 1 / (8 * 1_000_000_000),# Bit to Gigabyte
        6: 1 / (8 * 1_000_000_000_000), # Bit to Terabyte
    }

    return value * factors.get(selection_2, 0)


def byte_dictionary(selection_2, value):
    conversions = {
        1: value * 8,                             # to bit
        3: value / 1_000,                         # to kilobyte
        4: value / 1_000_000,                     # to megabyte
        5: value / 1_000_000_000,                 # to gigabyte
        6: value / 1_000_000_000_000,             # to terabyte
    }
    return conversions.get(selection_2, "Invalid conversion")

def kilobyte_dictionary(selection_2, value):
    conversions = {
        1: value * 8 * 1_000,                     # to bit
        2: value * 1_000,                         # to byte
        4: value / 1_000,                         # to megabyte
        5: value / 1_000_000,                     # to gigabyte
        6: value / 1_000_000_000,                 # to terabyte
    }
    return conversions.get(selection_2, "Invalid conversion")

def megabyte_dictionary(selection_2, value):
    conversions = {
        1: value * 8 * 1_000_000,                 # to bit
        2: value * 1_000_000,                     # to byte
        3: value * 1_000,                         # to kilobyte
        5: value / 1_000,                         # to gigabyte
        6: value / 1_000_000,                     # to terabyte
    }
    return conversions.get(selection_2, "Invalid conversion")

def gigabyte_dictionary(selection_2, value):
    conversions = {
        1: value * 8 * 1_000_000_000,             # to bit
        2: value * 1_000_000_000,                 # to byte
        3: value * 1_000_000,                     # to kilobyte
        4: value * 1_000,                         # to megabyte
        6: value / 1_000,                         # to terabyte
    }
    return conversions.get(selection_2, "Invalid conversion")

def terabyte_dictionary(selection_2, value):
    conversions = {
        1: value * 8 * 1_000_000_000_000,         # to bit
        2: value * 1_000_000_000_000,             # to byte
        3: value * 1_000_000_000,                 # to kilobyte
        4: value * 1_000_000,                     # to megabyte
        5: value * 1_000,                         # to gigabyte
    }
    return conversions.get(selection_2, "Invalid conversion")