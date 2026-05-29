from classs import Class
import json
import os

class Classes:
    def __init__(self):
        self.class_list = []

    def add_class(self):
        while True:
            course_name = input("Enter Course name: ")
            course_code = input("Enter course code: ")
            days = input("Enter class days: ")
            time = input("Enter class time: ")
            location = input("Enter class location: ")

            c = Class(
                course_name,
                course_code,
                days, time,
                location
            )
            self.class_list.append(c)
            self.save_classes()

            choice = input("\nEnter 1 if you'd like to add another class: ")

            if choice != '1':
                break
    
    def remove_class(self):
        while True:
            choice = input("Do you want to remove this class Y/N? ")
            choice = choice.upper()
            if choice == 'Y':
                index = int(input('What is the index of the class you wish to delete? '))
                self.class_list.pop(index - 1)
                self.save_classes()
                break
            elif choice == 'N':
                self.view_classes()
                break
            else:
                print("Enter 'Y' for yes and 'N' for no")


    def view_classes(self):
        for i, c in enumerate(self.class_list):
            print(f"{i + 1}. {c.course_name} | {c.days} | {c.time}")
        print(f"\n{len(self.class_list) + 1}. edit class")
        print(f"{len(self.class_list) + 2}. remove class")

        selection = int(input("Select a class/action or any number out of the index to go back to the main menu: "))
        if selection <= len(self.class_list):
            chosen_class = self.class_list[selection - 1]

            print(f'{chosen_class.to_string()}')
        elif (selection - 1) == len(self.class_list):
            self.edit_class()
        elif (selection - 2) == len(self.class_list):
            self.remove_class()
    
    def save_classes(self):
        data = []

        for c in self.class_list:
            data.append(c.to_dict())

        with open("classes.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_classes(self):
        with open("classes.json", "r") as file:
            data = json.load(file)

            for class_data in data:
                c = Class(
                    class_data["course_name"],
                    class_data["course_code"],
                    class_data["days"],
                    class_data["time"],
                    class_data["location"]
                )

                self.class_list.append(c)

    def display_edit_options(self):
        os.system("cls")
        print ("What do you wish to do to the selected class?\n")
        print('1. Change course name')
        print('2. Change course code')
        print('3. Change days')
        print('4. Change time')
        print('5. Change location')
        print('6. Back')
        print('\n')
    
    def edit_option_selection(self, selected_class):
        menu_option = int(input('Select a menu option 1 - 6: '))

        match menu_option:
            case 1:
                new_course_name = input('What do you wish to change the course name to: ')
                selected_class.set_course_name(new_course_name)
                self.save_classes()
            case 2:
                new_course_code = input('What do you wish to change the course code to: ')
                selected_class.set_course_code(new_course_code)
                self.save_classes()
            case 3:
                new_days = input('What do you wish to change the class days to: ')
                selected_class.set_days(new_days)
                self.save_classes()
            case 4:
                new_time = input('What do you wish to change the class time to: ')
                selected_class.set_time(new_time)
                self.save_classes()
            case 5:
                new_location = input('Where do you wish to change the class location to: ')
                selected_class.set_location(new_location)
                self.save_classes()
            case 6:
                print('Returning...')
                return False
            case _:
                print('Invalid option, pick a number between 1 - 6')

        input("\nPress Enter to continue...")


    def edit_class(self):
        choice_index = int(input("What's the index of the class you wish to edit? ")) - 1
        choice = self.class_list[choice_index]
        while True:
            os.system("cls")
            self.display_edit_options()

            if self.edit_option_selection(choice) == False:
                break


    
    

# Handled assignment logic. Error with load_assignment method which is affecting main. Clean up syntax and flow of the program 