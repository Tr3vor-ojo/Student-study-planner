import os

def display_menu():
    print ("Student planner\n")
    print('1. Add Assignment')
    print('2. View Assignments')
    print('3. Add Class')
    print('4. View Classes')
    print('5. View Calendar')
    print('6. Exit')
    print('\n')
    

def option_selection():
    menu_option = None
    menu_option = int(input('Select a menu option 1 - 6: '))

    match menu_option:
        case 1:
            os.system("cls")
        case 2:
            os.system("cls")
        case 3:
            os.system("cls")
        case 4:
            os.system("cls")
        case 5:
            os.system("cls")
        case 6:
            os.system("cls")
        case _:
            print('Invalid option, pick a number between 1 - 6')

            option_selection()


# display_menu()
# option_selection()