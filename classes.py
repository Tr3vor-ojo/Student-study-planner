from our_class import Class
import json
import os

class Classes:
    def __init__(self):
        self.class_list = []

    def add_class(self):
        while True:
            course_name = input("Enter Course name: ")
            course_code = input("Enter course code: ")
            days = input("Enter class days (e.g. Mon or Mon,Wed,Fri): ")
            days = days.upper()
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

            choice = input("\nEnter 1 if you'd like to add another class or any character to go back to the main menu: ")

            if choice != '1':
                break
    
    def remove_class(self):
        while True:
            choice = input("Do you want to remove this class Y/N? ")
            choice = choice.upper()
            if choice == 'Y':
                while True:
                    try:
                        index = int(input('What is the index of the class you wish to delete? '))
                        if index < 1 or index > len(self.class_list):
                            raise IndexError
                        
                        self.class_list.pop(index - 1)
                        self.save_classes()
                        break

                    except IndexError:
                        print('There is no class at that index.')

                    except ValueError:
                        print('Kindly enter a number.')

                break
            elif choice == 'N':
                self.view_classes()
                break
            else:
                print("Enter 'Y' for yes and 'N' for no")


    def view_classes(self):
        os.system("cls")
        while True:
            for i, c in enumerate(self.class_list):
                print(f"{i + 1}. {c.course_name} | {c.days} | {c.time}")
            print(f"\n{len(self.class_list) + 1}. edit class")
            print(f"{len(self.class_list) + 2}. remove class")
            print(f"{len(self.class_list) + 3}. back")
            while True:
                try:
                    selection = int(input("Select a class/action: "))
                    break
                except ValueError:
                    print('Kindly enter numbers only.')

            if selection < 1:
                break
            elif selection > (len(self.class_list)+3):
                print('There is nothing at that index.')
                continue
            elif selection <= len(self.class_list):
                os.system("cls")
                chosen_class = self.class_list[selection - 1]

                print(f'{chosen_class.to_string()}')
                input("\nPress Enter to continue...")
                os.system("cls")
            elif (selection - 1) == len(self.class_list):
                self.edit_class()
            elif (selection - 2) == len(self.class_list):
                self.remove_class()
            elif (selection - 3) == len(self.class_list):
                break
    
    def save_classes(self):
        data = []

        for c in self.class_list:
            data.append(c.to_dict())

        with open("classes.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_classes(self):
            try:
                with open("classes.json", "r") as file:
                    data = json.load(file)

            except FileNotFoundError:
                with open("classes.json", "w") as file:
                    json.dump([], file)

                data = []

            except json.JSONDecodeError:
                data = []

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
        while True:
            try:
                menu_option = int(input('Select a menu option 1 - 6: '))
                break
            except ValueError:
                print('Kindly enter a number.')

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
                new_days = new_days.upper()
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
        while True:
            try:
                choice_index = int(input("What's the index of the class you wish to edit? ")) - 1

                if choice_index < 0 or choice_index > len(self.class_list):
                    raise IndexError
                
                choice = self.class_list[choice_index]
                break
            except ValueError:
                print('Kindly enter a number.')

            except IndexError:
                print("There's no class at that index.")
        while True:
            os.system("cls")
            self.display_edit_options()

            if self.edit_option_selection(choice) == False:
                break

#fix indexerror for view assignment when selection is less negative