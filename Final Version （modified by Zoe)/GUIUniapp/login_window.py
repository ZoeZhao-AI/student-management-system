import os
import sys

current_path = os.path.dirname(__file__)
cli_root_path = os.path.abspath(os.path.join(current_path, "..", "CLIUniapp"))
sys.path.append(cli_root_path)

# login_window.py
import tkinter as tk
from tkinter import messagebox
from utils.validate import validate

def show_login(app):
    app.clear_window()
    app.root.title("Login Window")
    tk.Label(app.root, text="Please enter your email and password", font=("Arial", 16, "bold")).pack(pady=10)


    def add_row(label_text, show=""):
        row = tk.Frame(app.root)
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
        try:
            if not validate(email, password):
                raise ValueError("Email or password format is incorrect. Please try again.")
            student = app.db.get_email(email)
            if not student:
                raise LookupError("Your student email doesn't exist. Please try again.")
            if student.password != password:
                raise PermissionError("Incorrect password. Please try again.")
            app.current_student = student
            messagebox.showinfo("Success!", "Login successful")
            app.show_enrolment_window()
        except ValueError as ve:
            messagebox.showerror("Format Error", str(ve))
        except LookupError as le:
            messagebox.showerror("Email Error", str(le))
        except PermissionError as pe:
            messagebox.showerror("Password Error", str(pe))
        except Exception as e:
            messagebox.showerror("Unexpected Error", str(e))

    button_frame = tk.Frame(app.root)
    button_frame.pack(pady=10)
    tk.Button(button_frame, text="Login", command=attempt_login).pack(side="left", padx=5)
    tk.Button(button_frame, text="Back", command=app.show_main_menu).pack(side="left", padx=5)

