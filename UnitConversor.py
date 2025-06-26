#Unit Conversor
import os
from DistanceConversor import distance_dictionary
from TempConversor import  temp_dictionary
from WeightConversor import weight_dictionary

#Clearing terminal function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu(): 

    while True: 
        print('------------------')
        print('Select an option.')
        print('1. Convert')
        print('2. Exit')
        print('------------------')

        #When adding new features have to change some values
        option = int(input('Please, enter an option as an integer from 1 to 2: '))
        clear_screen()
        if option == 1:
            convert_menu()
        elif option == 2:
            break
        else:
            print('Option not valid, please, enter an option as an integer from 1 to 2')


def convert_menu(): #Menu to select a category of units of convertion

    
    #When adding new category have to change values from this 'while' statement.
    while True:
        clear_screen()

        print('------------------')
        print('   Convert Menu')
        print('------------------')
        print('Select a category.')
        print('1. Distance')
        print('2. Temperature')
        print('3. Weight')
        print('4. Return')
        print('------------------')

        option = int(input('Please, select a category between 1 and 3. Enter 4 to exit: '))
        if option == 4: break
        elif 0 < option <= 3:convert_selector(option)


def convert_selector(category: int):

    match category: #Set max selection index depending on the category of unit to make sure we only enter valid options excluding 'Exit' as an option.
        case 1:
            max = 6
        case 2:
            max = 3
        case 3:
            max = 5
    
        
    while True:
        display_menu(category) #Displays category's menu
        #Ask to enter valid options to make the conversions of the menu
        selection_1 = int(input(f'From 1 to {max}, enter your former type of unit. Enter {max + 1} to Exit: '))
        if selection_1 == max + 1: break 
        selection_2 = int(input(f'From 1 to {max}, enter the type of unit you want to convert to. Enter {max + 1} to Exit: '))
        if selection_2 == max + 1: break

        #Gatekeeper type logic
        if not 0 < selection_1 <= max and not 0 < selection_2 <= max:
            print(f'Both inputs were not valid, please enter an integer between 1 and {max}.')
        elif not 0 < selection_1 <= max :
            print(f'Input 1 not valid, please enter an integer between 1 and {max}.')
        elif not 0 < selection_2 <= max:
            print(f'Input 2 not valid, please enter an integer between 1 and {max}.')
        elif not selection_1 != selection_2:
            print('Wait, that is illegal!')
        else: #If everyting is fine we continue
            #Ask for the value of the unit to convert 
            value = float(input(f'Enter the value in {readable_unit(category, selection_1)} to convert it to {readable_unit(category, selection_2)}: '))

            match category: #Makes the convertions 
                case 1:
                    category_Dictionary = distance_dictionary(selection_1, selection_2, value)
                case 2:
                    category_Dictionary = temp_dictionary(selection_1, selection_2, value)
                case 3:
                    category_Dictionary = weight_dictionary(selection_1, selection_2, value)
        
            category_Dictionary #Calls the respective convertion method

def readable_unit(category: int,index : int): 
    # Returns the readable name of a unit based on its category and index selection

    match category:
        case 1:
            dictionary = ['404', 'meter/s',  'cm/s', 'Km/s', 'mile/s', 'foot/s', 'inch/s']
        case 2: 
            dictionary = ['404', 'Celsius (C)', 'Fahrenheit (F)', 'Kelvin (k)']
        case 3:
            dictionary = ['404', 'Gram/s (g)', 'Kilogram/s (kg)', 'Milligram/s (mg)', 'Pound/s (lb)', 'Ounces (Oz)']
    
    return dictionary[index]

def display_menu(category): #Function to display the respective menu
    clear_screen()
    match category:
        case 1:
            print('------------------')
            print('  Distance Menu')
            print('------------------')
            print('1. Meter (m)')
            print('2. Centimeter (cm)')
            print('3. Kilometer')
            print('4. Mile')
            print('5. Foot')
            print('6. Inch')
            print('7.Return')
            print('------------------')
        case 2:
            print('------------------')
            print(' Temperature Menu')
            print('------------------')
            print('1. Celsius (C)')
            print('2. Fahrenheit (F)')
            print('3. Kelvin (K)')
            print('4. Exit')
            print('------------------')
        case 3: 
            print('------------------')
            print('    Weight Menu ')
            print('------------------')
            print('1. Gram (g)')
            print('2. Kilogram (kg)')
            print('3. Milligram (mg)')
            print('4. Pound (lb)')
            print('5. Ounce (oz)')
            print('6. Exit')
            print('------------------')
        case _: print('Error while displaying the menu')


if __name__ == '__main__':
    main_menu()
    