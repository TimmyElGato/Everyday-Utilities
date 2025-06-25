#Unit Conversor
import os
from DistanceConversor import DistanceDictionary, StrDistanceOptions
from TempConversor import StrTempOptions, TempDictionary

#Clearing terminal function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def ConversorMenu(): 
    while True: 
        print('------------------')
        print('Select an option.')
        print('1. Convert')
        print('2. Exit')
        print('------------------')
        option = int(input())
        clear_screen()
        if option == 1:
            ConvertSelector()
        elif option == 2:
            break
        else:
            print('Option not valid.')


def ConvertSelector():
    while True: 
        
        clear_screen()
        print('------------------')
        print('Select a category.')
        print('1.Distance')
        print('2.Temperature')
        print('3.Weight')
        print('4.Return')
        print('------------------')

        option = int(input())
        if option == 1:
            DistanceSelector()
        elif option == 2:
            TempSelector()
        elif option == 3:
            WeightSelector()
        elif option == 4:
            break

# TODO : Implement Weight Selector
def WeightSelector():
    pass 


def TempSelector():
    while True:

        clear_screen() 
        print('------------------')
        print(' Temperature Menu')
        print('------------------')
        print('1. Celcius (C)')
        print('2. Fahrenheit (F)')
        print('3. Kelvin (K)')
        print('4. Return')
        print('------------------')

        opt_unit_1 = int(input('Select your former unit. (1 - 3). 4 to Exit: '))
        if opt_unit_1 == 4: break
        opt_unit_2 = int(input('Select the unit you want to convert to.(1 - 3). 4 to Exit: '))
        if opt_unit_2 == 4: break


        if opt_unit_1 != opt_unit_2 and 0 < opt_unit_1 <= 3 and 0 < opt_unit_2 <= 3:
            unit_1 = float(input(f'Enter the value in {StrTempOptions(opt_unit_1)} to convert it to {StrTempOptions(opt_unit_2)}:'))
            TempDictionary(opt_unit_1, opt_unit_2, unit_1)
        else:
            print('Options not valid')



def DistanceSelector():

    while True:

        clear_screen()
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

        opt_unit_1 = int(input('Select your former unit. (1 - 6). 7 to Exit: '))
        if opt_unit_1 == 7: break
        opt_unit_2 = int(input('Select the unit you want to convert to.(1 - 6). 7 to Exit: '))
        if opt_unit_2 == 7: break
        
        
        if opt_unit_1 != opt_unit_2 and 0 < opt_unit_1 <= 6 and 0 < opt_unit_2 <= 6:
            unit_1 = float(input(f'Enter the value in {StrDistanceOptions(opt_unit_1)} to convert it to {StrDistanceOptions(opt_unit_2)}:'))
            DistanceDictionary(opt_unit_1, opt_unit_2, unit_1)
        else:
            print('Options not valid')
        
       


if __name__ == '__main__':
    ConversorMenu()
            