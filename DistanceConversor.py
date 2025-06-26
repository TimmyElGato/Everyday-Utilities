def readable_distance(option):
    dictionary = ['meter/s', 'cm/s', 'Km/s', 'mile/s', 'foot/s', 'inch/es']
    return dictionary[option - 1]   
        
def distance_dictionary(selection_1, selection_2, value):
    Message(value, selection_1, selection_2)
    input('Enter any key to continue...')

def Message(value, selection_1, selection_2):
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

    print(f'{value} {readable_distance(selection_1)} converted to {readable_distance(selection_2)} is: {func:.2f} {readable_distance(selection_2)}')

def meter_dictionary(selection_2, value):
    match selection_2:
        case 2: #Centimeters
            return(value * 100)
        case 3: #Kilometrers
            return(value / 1000)
        case 4: #Miles
            return(value * 1609.344)
        case 5: #Foot
            return(value * 3.2808399)
        case 6: #Inches
            return(value * 39.3700787)


def centimeter_dictionary(selection_2, value):
    match selection_2:
        case 1: #Meters
            return (value / 100)
        case 3: #Kilometers
            return (value / 100000)
        case 4: #Miles
            return (value / 160934.4)
        case 5: #Foot
            return (value / 30.48)
        case 6: #Inches
            return (value / 2.54)

    
def kilometer_dictionary(selection_2, value):
    match selection_2:
        case 1: #Meters
            return(value * 1000)
        case 2: #Centimeters
            return(value * 1000000)
        case 4: #Miles
            return(value * 1.609344)
        case 5: #Foot
            return(value * 3280.8399)
        case 6: #Inches
            return(value * 39370.0787)
        
def mile_dictionary(selection_2, value):
    match selection_2:
        case 1: #Meters
            return(value * 1609.344)
        case 2: #Centimeters
            return(value * 160934.4)
        case 3: #Kilometers
            return(value * 1.609344)
        case 5: #Foot
            return(value * 5280)
        case 6: #Inches
            return(value * 63360)
        
def foot_dictionary(selection_2, value):
    match selection_2:
        case 1: #Meters
            return(value * 0.3048)
        case 2: #Centimeters
            return(value * 30.48)
        case 3: #Kilometers
            return(value * 0.0003048)
        case 4: #Miles
            return(value * 0.000189394)
        case 6: #Inches
            return(value * 12)

def inch_dictionary(selection_2, value):
    match selection_2:
        case 1: #Meters
            return(value * 0.0254)
        case 2: #Centimeters
            return(value * 2.54)
        case 3: #Kilometers
            return(value * 0.0000254)
        case 4: #Miles
            return(value * 0.0000157828)
        case 5: #Foot
            return(value * 0.0833333) 
        
