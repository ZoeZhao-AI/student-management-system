import os
import sys

# Add CLIUniApp folder to system path so we can import from model
current_path = os.path.dirname(__file__)
cli_root_path = os.path.abspath(os.path.join(current_path, "..", "CLIUniapp"))
sys.path.append(cli_root_path)

# GUI: Enrolment Window
import tkinter as tk
from tkinter import messagebox
from model.subject import Subject

def show_enrolment_window(app):
    app.clear_window()
    app.root.title("Enrolment Window")

    # Title label
    tk.Label(app.root, text="Your Enrollments", font=("Arial", 16, "bold")).pack(pady=10)

    # Function to handle enrolment
    def enrol_subject():
        if len(app.current_student.subjects) >= 4:
            messagebox.showerror("Warning!", "You can only enrol in up to 4 subjects")
            return

        new_subject = Subject()
        if app.current_student.get_subject(new_subject.id):
            messagebox.showerror("Warning!", "Subject already enrolled")
            return

        app.current_student.subjects.append(new_subject)
        app.db.save_students()
        messagebox.showinfo("Success", f"You have enrolled in subject {new_subject.id}")
        app.show_enrolment_window()

    # === Button layout row ===
    button_row = tk.Frame(app.root)
    button_row.pack(fill="x", padx=20, pady=10)

    # Left-aligned Enrol button
    tk.Button(button_row, text="Enrol Subject", command=enrol_subject).pack(side="left", anchor="w")

    # Right-aligned View and Back buttons (stacked vertically, left-aligned inside)
    right_button_frame = tk.Frame(button_row)
    right_button_frame.pack(side="right", anchor="e")
    tk.Button(right_button_frame, text="View Subjects", command=app.show_subject_window).pack(anchor="w", pady=2)
    tk.Button(right_button_frame, text="Back", command=app.show_main_menu).pack(anchor="w", pady=2)

    # === Display current enrolled subjects ===
    if app.current_student.subjects:
        subject_list_frame = tk.Frame(app.root)
        subject_list_frame.pack(anchor="w", padx=20, pady=10)

        tk.Label(subject_list_frame, text="Your Current Subjects:", font=("Arial", 14, "bold")).pack(anchor="w")

        # Each subject row includes label and remove button
        for subject in app.current_student.subjects:
            row = tk.Frame(subject_list_frame)
            row.pack(anchor="w", pady=2)
            tk.Label(row, text=f"Subject ID: {subject.id}", font=("Arial", 14)).pack(side="left")
            tk.Button(
                row,
                text="Remove",
                command=lambda s=subject: remove_specific_subject(app, s),
                bg="tomato",
                fg="white"
            ).pack(side="left", padx=10)

# Function to remove a subject and refresh the view
def remove_specific_subject(app, subject):
    if subject in app.current_student.subjects:
        app.current_student.subjects.remove(subject)
        app.db.save_students()
        app.show_enrolment_window()

    