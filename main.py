import os
from assignments import Assignments
from classes import Classes
from calendar import Calendar

ass = Assignments()
ass.load_assignments()
cla = Classes()
cla.load_classes()
cal = Calendar(cla)


def display_menu():
    os.system("cls")
    print ("Student planner\n")
    print('1. Add Assignment')
    print('2. View Assignments')
    print('3. Add Class')
    print('4. View Classes')
    print('5. View Calendar')
    print('6. Exit')
    print('\n')
    

def option_selection():
    while True:
        try:
            menu_option = int(input('Select a menu option 1 - 6: '))
            break
        except ValueError:
            print("Please enter a valid number")

    match menu_option:
        case 1:
            os.system("cls")
            ass.add_assignment()
            ass.save_assignments()
        case 2:
            os.system("cls")
            ass.view_assignments()
        case 3:
            os.system("cls")
            cla.add_class()
            cla.save_classes()
        case 4:
            os.system("cls")
            cla.view_classes()
        case 5:
            os.system("cls")
            cal.view_calendar()
        case 6:
            print('Goodbye User :)')
            return False
        case _:
            print('Invalid option, pick a number between 1 - 6')



while True:

    display_menu()

    if option_selection() == False:
        break
