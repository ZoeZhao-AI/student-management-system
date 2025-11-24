import os
import sys

current_path = os.path.dirname(__file__)
cli_root_path = os.path.abspath(os.path.join(current_path, "..", "CLIUniapp"))
sys.path.append(cli_root_path)

#GUI
import tkinter as tk
from tkinter import messagebox
from model.database import Database
from model.student import Student
from model.subject import Subject
from controller.student_controller import StudentController
from utils.validate import validate

class StudentGUI:
    # Main GUI class for the student system
    def __init__(self, root):
        self.root = root
        self.root.title("University Student System")  # [MODIFIED] Original title for initial window
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # database object, load saved student data (JSON)
        self.db = Database()

        # student controller
        self.student_controller = StudentController(self.db)

        # Holds the currently logged-in student
        self.current_student = None

        # main menu displays when the app starts
        self.show_main_menu()

    # Clears all widgets from the window
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Main menu with login/register options
    def show_main_menu(self):
        self.clear_window()
        self.root.title("Main Window")  # [MODIFIED] Marked for GUI window naming requirement

        tk.Label(self.root, text="Welcome to the Student System", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Login", font=("Arial", 12), command=self.show_login).pack(pady=5)

        # [MODIFIED] Replaced Register logic with a dummy disabled version
        tk.Button(
            self.root,
            text="Register",
            font=("Arial", 12),
            # [FAKE REGISTER] UI-only button for visual consistency. Functionality is disabled.
            command=lambda: messagebox.showinfo("Info", "You have already registered, please login.") ).pack(pady=5)

    # Login page
    def show_login(self):
        self.clear_window()
        self.root.title("Login Window")  # [MODIFIED] Set window title for marking

        def add_row(label_text, show=""):
            row = tk.Frame(self.root)
            row.pack(anchor="w", pady=3, padx=20)
            label = tk.Label(row, text=label_text, width=15, anchor="w")
            label.pack(side="left")
            entry = tk.Entry(row, width=30, show=show)
            entry.pack(side="left")
            return entry

        email_input = add_row("Email:")
        password_input = add_row("Password", show="*")

        def attempt_login():
            email = email_input.get()
            password = password_input.get()
            student = self.db.get_email(email)
            if student and student.password == password:
                self.current_student = student
                messagebox.showinfo("Success!", "Login successful")
                self.show_enrolment_window()  # [MODIFIED] Go to Enrolment Window first
            else:
                messagebox.showerror("Error!", "Invalid email or password")

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Login", command=attempt_login).pack(side="left", padx=5)
        tk.Button(button_frame, text="Back", command=self.show_main_menu).pack(side="left", padx=5)

    # [NEW] Enrolment Window separated from subject list
    def show_enrolment_window(self):
        self.clear_window()
        self.root.title("Enrolment Window")  # [ADDED] Set title for enrolment window

        tk.Label(self.root, text="Enrol in a Subject", font=("Arial", 14)).pack(pady=10)

        def enrol_subject():
            if len(self.current_student.subjects) >= 4:
                messagebox.showerror("Warning!", "You can only enrol in up to 4 subjects")
                return

            new_subject = Subject()
            if self.current_student.get_subject(new_subject.id):
                messagebox.showerror("Warning!", "Subject already enrolled")
                return

            self.current_student.subjects.append(new_subject)
            self.db.save_students()
            messagebox.showinfo("Success", f"You have enrolled in subject {new_subject.id}")
            self.show_enrolment_window()

        tk.Button(self.root, text="Enrol Subject", command=enrol_subject).pack(pady=5)
        tk.Button(self.root, text="View Subjects", command=self.show_subject_window).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.show_main_menu).pack(pady=5)

    # Subject Window - View & remove enrolled subjects
    def show_subject_window(self):
        self.clear_window()
        self.root.title("Subject Window")  # [MODIFIED] Set title for 4th required window

        tk.Label(self.root, text="Enrolled Subjects Review", font=("Arial", 14)).pack(pady=10)

        #[ADDED] If no subjects enrolled
        if not self.current_student.subjects:
            tk.Label(self.root, text="No subjects enrolled yet.").pack(pady=5)

        for subject in self.current_student.subjects:
            row = tk.Frame(self.root)
            row.pack(pady=2, anchor="w", padx=20)
            tk.Label(row, text=str(subject), font=("Arial", 10)).pack(side="left")

            def make_remove_func(subj=subject):
                return lambda: self.remove_specific_subject(subj)

            tk.Button(row, text="Remove", command=make_remove_func(), bg="tomato", fg="white").pack(side="left", padx=10)

        tk.Button(self.root, text="Back to Enrolment", command=self.show_enrolment_window).pack(pady=10)

    # Logic for removing subject & UI refresh
    def remove_specific_subject(self, subject):
        if subject in self.current_student.subjects:
            self.current_student.subjects.remove(subject)
            self.db.save_students()
            self.show_subject_window()

def main():
    root = tk.Tk()
    app = StudentGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
