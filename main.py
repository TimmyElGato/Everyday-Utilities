from MyFunctions import display_menu
from UnitConversor import convert_menu
from BinaryConversor import binary_menu

def main_menu(): 
    #IMPORTANT: Change when adding a new option!
    m_menu_options = ['Everyday Utilities!', 'Unit Conversor', 'Binary Conversor']
    len_m_menu = len(m_menu_options)
    
    while True: 
        display_menu(m_menu_options)
        option = int(input(f'Please, enter an option as an integer from 1 to {len_m_menu - 1}. Enter {len_m_menu} to exit: '))
        if option == 1:
            convert_menu()
        elif option == 2:
            binary_menu()
        elif option == len_m_menu:
            break

if __name__ == "__main__":
    main_menu()