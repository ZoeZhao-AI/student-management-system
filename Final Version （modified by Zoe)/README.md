
# Fundamental of Software Development
# Autumn 2025, Cmp1 – Lab 07 – Group 04 
# CLIUniApp and GUIUniApp – UTS Assessment 1 (Part 2 & 3)

## Group info

> Group Name: group04  
> Submission File: `group04-Cmp1lab07.zip`


|Student ID     | Name          | Contributions                                            |
|---------------|---------------|----------------------------------------------------------|
| 25616614      | Junseog Lee   | Subject class, Subject Controller class                  |
| 25499409      | Victor Ye     | Student class, Student Controller class, Database class  |
| 25531005      | Rohan Chauhan | Admin Controller class, Database class                   |
| 25719752      | Zoe Zhao      | GUI design and code                                      |

Specifically:
Junseog Lee (25616614)
-Developed the Subject class, which encapsulates the subject's data attributes such as subject ID, name, mark, and grade.
-Implemented the SubjectController class to manage subject-related operations including enrolment logic, grade calculation, and validation of subject limits.
-Ensured smooth interaction between the student interface and subject functionality, contributing to both CLI and GUI integration.

Victor Ye (25499409)
-Designed and implemented the Student class, which models student attributes (ID, name, email, password, and enrolled subjects).
-Developed the StudentController class to handle student-specific operations including registration, login, password updates, and subject management.
-Collaborated with Rohan to build the Database class responsible for storage and retrieval of student data via JSON. 
-Applied regular expression logic to validate student email and password formats as per the defined constraints.

Rohan Chauhan (25531005)
-Authored the AdminController class, which provides administrative functionalities such as viewing all students, grouping by grades, filtering pass/fail categories, and deleting records.
-Collaborated with Victor to build the Database class responsible for storage and retrieval of student data via JSON.Ensured reliable data syncing between CLI and GUI applications.
-Built a separate GUI system independently.

Zoe Zhao (25719752)
-Focused on the GUI design, including layout organization and widget configuration for login, subject enrolment, and grade viewing interfaces.
-Focused on enhancing visual clarity, usability, and form validation within the login_window, enrolment_window, and subject_window modules.
-Lead in GUI testing and debugging to ensure all graphical components function correctly and align with CLI system behavior.
-Developed the University System menu, including role selection(student/admin) and linking the student systme into the overall application

## Prerequisites
- Python 3.9+
- tkinter (built-in for GUI)
- Install `colorama` if not available: `pip install colorama`
- No external libraries required

---
## Project Overview
This is a team project for the University of Technology Sydney (UTS) Assessment 1 – Part 2 & 3. It implements both a Command Line Interface (CLI) and a Graphical User Interface (GUI) application for a university student management system. 

---
## Key Features
### Student System
- Register and login (email/password format validation using RegEx)
- Enrol up to 4 subjects (auto-generated marks and grades)
- Change password
- View enrolled subjects and grades
- Remove subject

### Admin System
- Show all students
- Group students by grade (HD/D/C/P/F)
- Partition students into PASS/FAIL categories
- Remove individual students by ID
- Clear entire database

### GUIUniApp (Challenge Task)
- GUI login for registered students only
- Subject enrolment interface (up to 4 subjects)
- View marks/grades
- Input validation & exception handling
- Student data synced with CLI system (shared `students.data`)
---

## Project Structure

```
project_root/
    CLIUniapp/
        main.py                     # Main entry point for CLI
        README.md                   # This file

        model/
            database.py             # Reads/writes student data from/to
            student.py              # Student model
            subject.py              # Subject model (ID, mark, grade)

        controller/
            admin_controller.py     # Handles admin-side CLI logic
            student_controller.py   # Handles student-side CLI logic
            subject_controller.py   # Handles subject-side CLI logic
        utils/
            validate.py             # validation function for student email and password
        data/
            students.data           # Data file where all student info is stored

    GUIUniapp/
        main.py                 # GUI Entry point (login window)
        login_window.py             # Window for logging registering/logging in
        enrolment_window.py         # Window for enrolling subjects
        subject_window.py           # Displays enrolled subjects
---


## How to Run
The program executed via the main.py.
1. Download group04-Cmp1lab07.
2. Extract files to Downloads folder.
3. Import files into Vscode.
4. Navigate to CLIUniapp/main.py to run CLI.
5. Navigate to GUIUniapp/main.py to run GUI.


## Notes
- All data is saved in `students.data` (JSON format)
- Student emails must end in '@university.com'
- Student passwords must begin with a capital letter, consist of at least 5 letters, followed by at least 3 digits.
- Students and Admins access are strictly separated
- GUI and CLI both read/write from the same student database

---

