import os
import sys

current_path = os.path.dirname(__file__)
cli_root_path = os.path.abspath(os.path.join(current_path, "..", "CLIUniapp"))
sys.path.append(cli_root_path)

# main_app.py
import tkinter as tk
from tkinter import messagebox
from model.database import Database
from controller.student_controller import StudentController

from main_window import show_main_menu
from login_window import show_login
from enrolment_window import show_enrolment_window
from subject_window import show_subject_window
from enrolment_window import remove_specific_subject

class StudentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("University Student System")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.db = Database()
        self.student_controller = StudentController(self.db)
        self.current_student = None

        self.show_main_menu = lambda: show_main_menu(self)
        self.show_login = lambda: show_login(self)
        self.show_enrolment_window = lambda: show_enrolment_window(self)
        self.show_subject_window = lambda: show_subject_window(self)
        self.remove_specific_subject = lambda subject: remove_specific_subject(self, subject)

        self.clear_window()
        self.show_main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentGUI(root)
    root.mainloop()
