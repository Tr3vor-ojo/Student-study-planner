from assignment import Assignment
import json
import os

class Assignments:
    def __init__(self):
        self.assignment_list = []


    def add_assignment(self, assignment):
        self.assignment_list.append(assignment)
        self.save_assignments()

    def remove_assignment(self, index):
        self.assignment_list.pop(index - 1)
        self.save_assignments()


    
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
                    assignment_data["priority"],
                    assignment_data["completed_status"]
                )

                self.assignment_list.append(assignment)


    def update_assignment(self, assignment, field, value):
        if field == "priority":
            value = value.upper()
        allowed = {"title", "course", "due_date", "priority", "completed_status"}
        if field not in allowed:
            raise ValueError(f"Unknown field: {field}")
        setattr(assignment, field, value)
        self.save_assignments()

 