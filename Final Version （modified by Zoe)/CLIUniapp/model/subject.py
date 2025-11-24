import random

class Subject:

    def __init__(self):
        self.id = self.id_generator()
        self.mark = self.mark_generator()
        self.grade = self.grade_checker()

    def id_generator(self):
        return f"{random.randint(1,999):03}"

    def mark_generator(self):
        return random.randint(25, 100)

    def grade_checker(self):
        if self.mark >= 85:
            return "HD"
        elif self.mark >= 75:
            return "D"
        elif self.mark >= 65:
            return "C"
        elif self.mark >= 50:
            return "P"
        else:
            return "F"

    def __str__(self):
        return f"[ Subject :: {self.id:<7} -- Mark =  {self.mark:<5} -- Grade = {self.grade:<3} ]"