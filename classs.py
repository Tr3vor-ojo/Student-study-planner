class Class:
    def __init__(self, course_name, course_code, days, time, location):
        self.course_name = course_name
        self.course_code = course_code
        self.days = days
        self.location = location
        self.time = time

    def to_dict(self):
        return {
            "course_name": self.course_name,
            "course_code": self.course_code,
            "days": self.days,
            "time": self.time,
            "location": self.location
        }

    def to_string(self):
        return (
            f"course_name: {self.course_name}\n"
            f"course_code: {self.course_code}\n"
            f"days: {self.days}\n"
            f"time: {self.time}\n"
            f"location: {self.location}"
        )
    
    def set_course_name(self, cn):
        self.course_name = cn
    
    def set_course_code(self, cc):
        self.course_code = cc

    def set_days(self, d):
        self.days = d

    def set_time(self, t):
        self.time = t
    
    def set_location(self, l):
        self.location = l

        


