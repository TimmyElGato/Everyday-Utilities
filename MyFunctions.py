import os
#Clearing terminal function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu(options): #Function to display the respective menu
    
    clear_screen()
    line_width = 25 #width of the decoration lines for the titles of the menus

    for i, option in enumerate(options):
        if i == 0: #If its the name of the menu (the first value of the list):
            print('-' * line_width) #Decoration lines
            print(option.center(line_width))
            print('-' * line_width) 
        else:
            print(f'{i}. {option}')
    print(f'{len(options)}. Exit') #At the end we print the 'Exit' option. 