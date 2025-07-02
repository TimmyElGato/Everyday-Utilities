#Unit Conversor
from MyFunctions import display_menu
from DistanceConversor import distance_dictionary
from TempConversor import  temp_dictionary
from WeightConversor import weight_dictionary
from TimeConversor import time_dictionary
from DataConversor import data_dictionary


def convert_menu(): #Menu to select a category of units of convertion

    #IMPORTANT: When adding a new category have to make changes here 1/4!
    convert_options = ['Convert Menu!', 'Distance', 'Temperature', 'Weight', 'Time', 'Data']
    len_options = len(convert_options)

    while True:

        display_menu(convert_options)

        option = int(input(f'Please, select a category between 1 and {len_options - 1}. Enter {len_options} to exit: '))

        if option == len_options : break
        elif 0 < option <= len_options: convert_selector(option)


def convert_selector(category: int):

    #IMPORTANT: When adding a new category have to make changes here 2/4!
    match category: #This sets the options for the 'display_menu' function
        case 1:
            options = ['Distance Menu', 'Meter (m)', 'Centimeter (cm)', 'Kilometer (km)', 'Mile', 'Foot', 'Inch']
        case 2:
            options = ['Temperature Menu', 'Celcius (C)','Fahrenhei (F)', 'Kelvin (K)' ]
        case 3:
            options = ['Weight Menu', 'Gram (g)', 'Kilogram (kg)', 'Milligram (mg)', 'Pound (lb)', 'Ounce (oz)']
        case 4:
            options = ['Time Menu', 'Second/s', 'Minute/s', 'Hour/s', 'Day/s', 'Week/s', 'Month/s', 'Year/s']
        case 5:
            options ['Data Menu', 'Bit', 'Byte', 'Kilobyte (KB)', 'Megabyte (MB)', 'Gigabyte (GB)', 'Terabyte (TB)']

    max = len(options) - 1
        
    while True:
        display_menu(options) #Displays category's menu
        #Ask to enter valid options to make the conversions of the menu
        selection_1 = int(input(f'From 1 to {max}, choose the unit you want to convert from. Enter {max + 1} to Exit: '))
        if selection_1 == max + 1: break 
        selection_2 = int(input(f'From 1 to {max}, choose the unit you want to convert to. Enter {max + 1} to Exit: '))
        if selection_2 == max + 1: break

        #Gatekeeper type logic
        if not 0 < selection_1 <= max : #Checks if selection 1 is between the limits of the options 
            print(f'Input 1 not valid, please enter an integer between 1 and {max}.')
        elif not 0 < selection_2 <= max: #Checks if selection 2 is between the limits of the options 
            print(f'Input 2 not valid, please enter an integer between 1 and {max}.')
        elif not selection_1 != selection_2: #Checks if selections are different from each other
            print('Wait, that is illegal!')
        else: #If everyting is fine we continue

            #Ask for the value of the unit to convert 
            value = float(input(f'Enter the value in {readable_unit(category, selection_1)} to convert it to {readable_unit(category, selection_2)}: '))

            #IMPORTANT: When adding a new category have to make changes here 3/4
            match category: #Makes the convertions 
                case 1:
                    category_Dictionary = distance_dictionary(selection_1, selection_2, value)
                case 2:
                    category_Dictionary = temp_dictionary(selection_1, selection_2, value)
                case 3:
                    category_Dictionary = weight_dictionary(selection_1, selection_2, value)
                case 4:
                    category_Dictionary = time_dictionary(selection_1, selection_2, value)
                case 5:
                    category_Dictionary = data_dictionary(selection_1, selection_2, value)
        
            category_Dictionary #Calls the respective convertion method

def readable_unit(category: int, index : int): 
    # Returns the readable name of a unit based on its category and index selection
    
    match category: #IMPORTANT: When adding new category have to make changes here 4/4
        case 1:
            dictionary = ['404', 'meter/s',  'cm/s', 'Km/s', 'mile/s', 'foot/s', 'inch/s']
        case 2: 
            dictionary = ['404', 'Celsius (C)', 'Fahrenheit (F)', 'Kelvin (k)']
        case 3:
            dictionary = ['404', 'gram/s (g)', 'kilogram/s (kg)', 'milligram/s (mg)', 'pound/s (lb)', 'ounces (Oz)']
        case 4:
            dictionary = ['404', 'second/s', 'minute/s', 'hour/s', 'day/s', 'week/s', 'month/s', 'year/s']    
        case 5: 
            dictionary = ['404', 'Bit/s', 'Byte/s', 'Kilobyte/s (KB)', 'Megabyte/s (MB)', 'Gigabyte/s (GB)', 'Terabyte/s (TB)']
    
    return dictionary[index]

    