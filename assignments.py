from assignment import Assignment
import json
import os

class Assignments:
    def __init__(self):
        self.assignment_list = []

    def add_assignment(self):
        while True:
            title = input("Enter title: ")
            course = input("Enter course: ")
            due_date = input("Enter due date: ")
            temp = input("Enter assignment priority (low, mid or high): ")
            priority = temp.upper()

            assignment = Assignment(
                title,
                course,
                due_date,
                priority
            )
            self.assignment_list.append(assignment)
            self.save_assignments()

            choice = input("\nEnter 1 if you'd like to add another assignment or any character to go back to the main menu: ")

            if choice != '1':
                break
    
    def remove_assignment(self):
        while True:
            choice = input("Do you want to remove this assignment Y/N? ")
            choice = choice.upper()
            if choice == 'Y':
                while True:
                    try:
                        index = int(input('What is the index of the assignment you wish to delete? '))
                        if index < 1 or index > len(self.assignment_list):
                            raise IndexError
                        
                        self.assignment_list.pop(index - 1)
                        self.save_assignments()
                        break
                    except IndexError:
                        print('There is no assignment at that index.')
                    except ValueError:
                        print('Kindly enter a number.')
                break
            elif choice == 'N':
                self.view_assignments()
                break
            else:
                print("Enter 'Y' for yes and 'N' for no")


    def view_assignments(self):
        os.system("cls")
        while True:
            for i, assignment in enumerate(self.assignment_list):
                print(f"{i + 1}. {assignment.title} | Due: {assignment.due_date}")
            print(f"\n{len(self.assignment_list) + 1}. edit assignment")
            print(f"{len(self.assignment_list) + 2}. remove assignment")
            while True:
                try:
                    selection = int(input("Select an assignment/action or any number out of the index to go back to the main menu: "))
                    break
                except ValueError:
                    print('Kindly enter numbers only.')
            
            if selection < 1:
                break
            elif selection <= len(self.assignment_list):
                chosen_assignment = self.assignment_list[selection - 1]

                print(f'{chosen_assignment.to_string()}')
            elif (selection - 1) == len(self.assignment_list):
                self.edit_assignment()
            elif (selection - 2) == len(self.assignment_list):
                self.remove_assignment()
    
    def save_assignments(self):
        data = []

        for assignment in self.assignment_list:
            data.append(assignment.to_dict())

        with open("assignments.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_assignments(self):
            try:
                with open("assignments.json", "r") as file:
                    data = json.load(file)

            except FileNotFoundError:
                with open("assignments.json", "w") as file:
                    json.dump([], file)

                data = []

            except json.JSONDecodeError:
                data = []

            for assignment_data in data:
                assignment = Assignment(
                    assignment_data["title"],
                    assignment_data["course"],
                    assignment_data["due_date"],
                    assignment_data["priority"]
                )
                assignment.completed_status = assignment_data["completed_status"]

                self.assignment_list.append(assignment)

    def display_edit_options(self):
        os.system("cls")
        print ("What do you wish to do to the selected assignment\n")
        print('1. Change title')
        print('2. Change due date')
        print('3. Change course')
        print('4. Change priority')
        print('5. Change completed status')
        print('6. Back')
        print('\n')
    
    def edit_option_selection(self, assignment):
        while True:
            try:
                menu_option = int(input('Select a menu option 1 - 6: '))
                break
            except ValueError:
                print('Kindly enter a number.')

        match menu_option:
            case 1:
                new_title = input('What do you wish to change the title to: ')
                assignment.set_title(new_title)
                self.save_assignments()
            case 2:
                new_due_date = input('What do you wish to change the due date to: ')
                assignment.set_due_date(new_due_date)
                self.save_assignments()
            case 3:
                new_course = input('What do you wish to change the course to: ')
                assignment.set_course(new_course)
                self.save_assignments()
            case 4:
                new_priority = input('What do you wish to change the priority to: ')
                assignment.set_priority(new_priority)
                self.save_assignments()
            case 5:
                os.system("cls")
                print("1. Completed")
                print("2. Not Completed")
                while True:
                    try:
                        choice = int(input("Select an option: "))
                        break
                    except ValueError:
                        print('Kindly enter numbers only.')

                if choice == 1:
                    assignment.set_completed_status(True)

                elif choice == 2:
                    assignment.set_completed_status(False)

                self.save_assignments()
            case 6:
                print('Returning...')
                return False
            case _:
                print('Invalid option, pick a number between 1 - 6')

        input("\nPress Enter to continue...")


    def edit_assignment(self):
        while True:
            try:
                choice_index = int(input("What's the index of the assignment you wish to edit? ")) - 1

                if choice_index < 0 or choice_index >= len(self.assignment_list):
                    raise IndexError
                
                choice = self.assignment_list[choice_index]
                break

            except ValueError:
                print('Kindly enter a number.')

            except IndexError:
                print("There's no assignment at that index")
        while True:
            os.system("cls")
            self.display_edit_options()

            if self.edit_option_selection(choice) == False:
                break

 