class Assignment:
    def __init__(self, title, course, due_date, priority):
        self.title = title
        self.course = course
        self.due_date = due_date
        self.completed_status = False
        self.priority = priority

    def to_dict(self):
        return {
            "title": self.title,
            "course": self.course,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed_status": self.completed_status
        }

    def to_string(self):
        return (
            f"title: {self.title}\n"
            f"course: {self.course}\n"
            f"due_date: {self.due_date}\n"
            f"priority: {self.priority}\n"
            f"completed_status: {self.completed_status}"
        )