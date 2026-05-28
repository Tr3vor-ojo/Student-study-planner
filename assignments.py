from assignment import Assignment
import json
import os

class Assignments:
    def __init__(self):
        self.assignment_list = []

    def add_assignment(self):
        title = input("Enter title: ")
        course = input("Enter course: ")
        due_date = input("Enter due date: ")
        priority = int(input("Enter assignment priority: "))

        assignment = Assignment(title, course, due_date, priority)

        self.assignment_list.append(assignment)

        choice = int(input("\nEnter 1 if you'd like to add another assignment: "))
        if choice == 1:
            self.add_assignment()
    
    def remove_assignment(self):
        choice = input("Do you want to remove this assignment Y/N? ")
        if choice == 'Y':
            index = int(input('What is the index of the assignment you wish to delete? '))
            self.assignment_list.pop(index - 1)
            self.save_assignments()
        elif choice == 'N':
            self.view_assignments()
        else:
            print("Enter 'Y' for yes and 'N' for no")
            self.remove_assignment()


    def set_priority():
        None

    def view_assignments(self):
        for i, assignment in enumerate(self.assignment_list):
            print(f"{i + 1}. {assignment.title} | Due: {assignment.due_date}")
        print(f"\n{len(self.assignment_list) + 1}. remove assignment")

        selection = int(input("Select an assignment: "))

        chosen_assignment = self.assignment_list[selection - 1]

        print(f'{chosen_assignment.to_string()}')
    
    def save_assignments(self):
        data = []

        for assignment in self.assignment_list:
            data.append(assignment.to_dict())

        with open("assignments.json", "w") as file:
            json.dump(data, file, indent=4)

def load_assignments(self):
    with open("assignments.json", "r") as file:
        data = json.load(file)

        for assignment_data in data:
            assignment = Assignment(
                assignment_data["title"],
                assignment_data["course"],
                assignment_data["due_date"],
                assignment_data["priority"]
            )
            assignment.completed_status = assignment_data["completed_status"]

            self.assignment_list.append(assignment)

# Handled assignment logic. Error with load_assignment method which is affecting main. Clean up syntax and flow of the program 