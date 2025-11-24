import random

class Student:
    def __init__(self, name, email, password):
        self.id = self.id_generator()
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []

    def id_generator(self):
        return f"{random.randint(1,999999):06}"

    @property
    def average_mark(self):
        if self.subjects:
            return sum(sub.mark for sub in self.subjects) / len(self.subjects)
        return 0

    @property
    def average_grade(self):
        avg = self.average_mark
        if avg >= 85:
            return "HD"
        elif avg >= 75:
            return "D"
        elif avg >= 65:
            return "C"
        elif avg >= 50:
            return "P"
        else:
            return "F"

    @property
    def pass_status(self):
        if not self.subjects:
            return "F"
        return "P" if self.average_mark >= 50 else "F"

    def get_subject(self, id_):
        return next((sub for sub in self.subjects if sub.id == id_), None)

    def set_password(self, pd_):
        self.password = pd_


