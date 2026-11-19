import os, sys
from assignments import Assignments
from assignment import Assignment
from classes import Classes
from our_class import Class
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

def prompt_new_assignment():
    title = input("Enter title: ")
    course = input("Enter course: ")
    due_date = input("Enter due date: ")
    priority = input("Enter assignment priority (low, mid or high): ").upper()
    return Assignment(title, course, due_date, priority)


def prompt_remove_assignment():
    while True:
        choice = input("Do you want to remove an assignment Y/N? ").upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            print("Enter 'Y' for yes and 'N' for no")


def prompt_assignment_index(assignment_list):
    while True:
        try:
            index = int(input('What is the index of the assignment you wish to delete? '))
            if index < 1 or index > len(assignment_list):
                raise IndexError
            return index-1
        except IndexError:
            print('There is no assignment at that index.')
        except ValueError:
            print('Kindly enter a number.')

def prompt_edit_field():
    while True:
        try:
            option = int(input("Select a menu option 1 - 6: "))
            return option
        except ValueError:
            print("Kindly enter a number.")


def prompt_field_value(field):
    if field == "completed_status":
        while True:
            try:
                choice = int(input("1. Completed\n2. Not Completed\nSelect an option: "))
                if choice in (1, 2):
                    return choice == 1
            except ValueError:
                pass
            print("Enter 1 or 2.")
    return input(f"What do you wish to change the {field} to: ")


def prompt_new_class():
    course_name = input("Enter Course name: ")
    course_code = input("Enter course code: ")
    days = input("Enter class days (e.g. Mon or Mon,Wed,Fri): ")
    days = days.upper()
    time = input("Enter class time: ")
    location = input("Enter class location: ")
    return Class(course_name, course_code, days, time,location)




def option_selection():
    while True:
        try:
            menu_option = int(input('Select a menu option 1 - 6: '))
            break
        except ValueError:
            print("Please enter a valid number")

    match menu_option:
        case 1:#add assignment
            os.system("cls")
            while True:
                ass.add_assignment(prompt_new_assignment())
                if input("\nEnter 1 to add another, any other character to return: ") != '1':
                    break

        case 2: #view assignments
            os.system("cls")
            for i, a in enumerate(ass.assignment_list):
                print(f"{i + 1}. {a.title} | Due: {a.due_date}")

            EDIT   = len(ass.assignment_list) + 1
            REMOVE = len(ass.assignment_list) + 2
            BACK   = len(ass.assignment_list) + 3
            print(f"\n{EDIT}. edit assignment")
            print(f"{REMOVE}. remove assignment")
            print(f"{BACK}. back")

            while True:
                try:
                    selection = int(input("Select an assignment/action: "))
                    break
                except ValueError:
                    print('Kindly enter numbers only.')

            if 1 <= selection <= len(ass.assignment_list):
                print(ass.assignment_list[selection - 1].to_string())
                input("\nPress enter to continue...")
            elif selection == EDIT:
                FIELDS = {1: "title", 2: "due_date", 3: "course", 4: "priority", 5: "completed_status"}

                index = prompt_assignment_index(ass.assignment_list)
                chosen = ass.assignment_list[index]
                option = prompt_edit_field()
                
                if option == 6:
                    pass
                elif option in FIELDS:
                    field = FIELDS[option]
                    ass.update_assignment(chosen, field, prompt_field_value(field))
                else:
                    print('Invalid option, pick a number between 1 - 6')
            elif selection == REMOVE:
                if prompt_remove_assignment():
                    ass.remove_assignment(prompt_assignment_index(ass.assignment_list))
            elif selection == BACK:
                pass

        case 3:#add class
            os.system("cls")
            while True:
                cla.add_class(prompt_new_class())
                choice = input("\nEnter 1 if you'd like to add another class or any character to go back to the main menu: ")
                
                if choice != '1':
                    break

        case 4:#view classes
            os.system("cls")
            cla.view_classes()
        case 5:#view calendar
            os.system("cls")
            cal.view_calendar()
        case 6:#exit
            print('Goodbye User :)')
            return False
        case _:
            print('Invalid option, pick a number between 1 - 6')
    return True



while True:

    display_menu()

    if option_selection() == False:
        break
