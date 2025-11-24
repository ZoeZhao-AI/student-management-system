import json
import os
from model.student import Student
from model.subject import Subject

class Database:
    def __init__(self):
        self.students = []        
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Proejct Root
        self.file_path = os.path.join(base_dir, "data", "student.data")

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)
        self.load_students()


    def load_students(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.students = [self.dict_to_student(d) for d in data]
        except (json.JSONDecodeError, TypeError) as error:
            print("Error loading student data:", error)
            self.students = []

    def save_students(self):
        try:
            with open(self.file_path, "w") as file:
                json.dump([self.student_to_dict(s) for s in self.students], file, indent=4)
        except Exception as e:
            print(f"Failed to save student data: {e}")

    def add_student(self, student):
        self.students.append(student)
        self.save_students()

    def remove_one(self, student):
        self.students.remove(student)
        self.save_students()
        
    def remove_all(self):
        self.students.clear()
        self.save_students()


    def student_to_dict(self, student):
        return {
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "password": student.password,
            "subjects": [self.subject_to_dict(subject) for subject in student.subjects]
        }

    def subject_to_dict(self, subject):
        return {
            "id": subject.id,
            "mark": subject.mark,
            "grade": subject.grade
        }

    def dict_to_student(self, data):
        student = Student(data["name"], data["email"], data["password"])
        student.id = data["id"]
        student.subjects = [self.dict_to_subject(s) for s in data.get("subjects", [])]
        return student

    def dict_to_subject(self, data):
        subject = Subject()
        subject.id = data["id"]
        subject.mark = data["mark"]
        subject.grade = data["grade"]
        return subject



    def get_email(self, email_):
        return next((s for s in self.students if s.email == email_), None)

    def get_id(self, id_):
        return next((s for s in self.students if s.id == id_), None)

