# subject_window.py
import tkinter as tk

def show_subject_window(app):
    # Clear previous window content
    app.clear_window()
    app.root.title("Grades and Marks")  # Updated window title

    # Page heading
    tk.Label(app.root, text="Subject Grades Overview", font=("Arial", 16, "bold")).pack(pady=10)

    # If no subjects enrolled, show message
    if not app.current_student.subjects:
        tk.Label(app.root, text="No subjects enrolled yet.",font=("Arial", 14)).pack(pady=5)
    else:
        # Display each subject's details
        for subject in app.current_student.subjects:
            row = tk.Frame(app.root)
            row.pack(pady=2, anchor="w", padx=20)
            tk.Label(row, text=str(subject), font=("Arial", 14)).pack(side="left")

    # Back button to return to enrolment window
    tk.Button(app.root, text="Back to Enrolment", command=app.show_enrolment_window).pack(pady=10)
