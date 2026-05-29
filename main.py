import os
from assignment import Assignment
from assignments import Assignments
from classes import Classes

a1 = Assignments()
a1.load_assignments()
c1 = Classes()
c1.load_classes()

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
    menu_option = int(input('Select a menu option 1 - 6: '))

    match menu_option:
        case 1:
            os.system("cls")
            a1.add_assignment()
            a1.save_assignments()
        case 2:
            os.system("cls")
            a1.view_assignments()
        case 3:
            os.system("cls")
            c1.add_class()
            c1.save_classes()
        case 4:
            os.system("cls")
            c1.view_classes()
        case 5:
            os.system("cls")
        case 6:
            print('Goodbye User!')
            return False
        case _:
            print('Invalid option, pick a number between 1 - 6')



while True:

    display_menu()

    if option_selection() == False:
        break
