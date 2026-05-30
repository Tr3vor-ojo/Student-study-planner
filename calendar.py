class Calendar:
    def __init__(self, classes):
        self.classes = classes

    def view_calendar(self):
        schedule = {
            'MON': [],
            'TUE': [],
            'WED': [],
            'THU': [],
            'FRI': [],
            'SAT': [],
            'SUN': []
        }

        for c in self.classes.class_list:
            for day in c.days.split(','):
                day = day.strip()
                if day in schedule:
                    schedule[day].append(c)
                else:
                    print(f"Invalid day: {day}")
    
        for day in schedule:
            if schedule[day]:
                print(f'\n{day}')

                for c in schedule[day]:
                    print(f"{c.course_name} ({c.time})")

        input("\nPress Enter to go back to the main menu...")