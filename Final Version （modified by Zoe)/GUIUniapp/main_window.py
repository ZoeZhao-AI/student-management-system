# main_window.py
import tkinter as tk
from tkinter import messagebox

def show_main_menu(app):
    app.clear_window()
    app.root.title("Main Window")

    tk.Label(app.root, text="Welcome to the Student System", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Button(app.root, text="Login", font=("Arial", 12), command=app.show_login).pack(pady=5)

    # [FAKE REGISTER] UI-only button for visual consistency. Functionality is disabled.
    tk.Button(
        app.root,
        text="Register",
        font=("Arial", 12),
        command=lambda: messagebox.showinfo("Info", "You have already registered, please login.")
    ).pack(pady=5)