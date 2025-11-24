from colorama import Fore, init, Style

class AdminController:

    def __init__(self, db):
        self.db = db

    def menu(self):
        while True:
            try:
                choice = input(Fore.BLUE + "\tAdmin System (c/g/p/r/s/x): " + Style.RESET_ALL).lower()

                match choice:
                    case "c":
                        self.clear_file()
                    case "g":
                        self.group()
                    case "p":
                        self.partition()
                    case "r":
                        self.remove_student()
                    case "s":
                        self.show()
                    case "x":
                        break
                    case _:
                        print(Fore.YELLOW + "\t(c) clear database: Clear all data on students.data")
                        print(Fore.YELLOW + "\t(g) group students: Groups students by grade")
                        print(Fore.YELLOW + "\t(p) partition students: Partition students to PASS/FAIL categories")
                        print(Fore.YELLOW + "\t(r) remove student: Remove a student by ID")
                        print(Fore.YELLOW + "\t(s) show: Show all students")
                        print(Fore.YELLOW + "\t(x) exit")

            except KeyboardInterrupt:
                print(Fore.YELLOW + "\n\tInterrupted by user")
                break
            except Exception as e:
                print(Fore.YELLOW + f"\tUnexpected error: {e}")        


    def clear_file(self):
        try:
            print(Fore.YELLOW + "\tClearing students database")
            choice = input(Fore.RED + "\tAre you sure you want to clear the database (Y)ES / (N)O: "+ Style.RESET_ALL).upper()
            
            if choice == "Y":
                self.db.remove_all()
                print(Fore.YELLOW + "\tStudent data cleared")

        except Exception as e:
            print(Fore.YELLOW + f"\tUnexpected error: {e}")        

    def remove_student(self):
        try:
            id_ = input("\tRemove by ID: ")
            del_student = self.db.get_id(id_)
            
            if del_student:
                self.db.remove_one(del_student)
                print(Fore.YELLOW + f"\tRemoving Student {id_} Account")

            else:
                print(Fore.RED + f"\tStudent {id_} does not exist")

        except Exception as e:
            print(Fore.YELLOW + f"\tUnexpected error: {e}")        

    def show(self):
        print(Fore.YELLOW + "\tStudent List")
        if not self.db.students:
            print("\t\t< Nothing to Display >")
            return

        for student in self.db.students:
            print(f"\t{student.name:<10} :: {student.id:<7} --> Email: {student.email:<15}")        

    def group(self):
        print(Fore.YELLOW +"\tGrade Grouping")

        if not self.db.students:
            print("\t\t< Nothing to Display >")
            return

        grades = ["HD", "D", "C", "P", "F"]
        groups = {g: [] for g in grades}

        for student in self.db.students:
            groups[student.average_grade].append(student)

        for grade in grades:
            if groups[grade]:
                group_str = ", ".join(
                    f"{s.name:<10} :: {s.id:<7} --> GRADE: {grade:<3} - MARK: {s.average_mark:>5.2f}"
                    for s in groups[grade]
                )
                print(f"\t{grade} --> [{group_str}]")

    def partition(self):
        print(Fore.YELLOW + "\tPASS/FAIL Partition")

        passed = []
        failed = []

        for s in self.db.students:
            if s.pass_status == "P":
                passed.append(s)
            else:
                failed.append(s)

        fail_line = ", ".join(
            f"{s.name:<10} :: {s.id:<7} --> GRADE: {s.average_grade:<3} - MARK: {s.average_mark:>5.2f}" for s in failed
        )
        print(f"\tFAIL --> [{fail_line}]")

        pass_line = ", ".join(
            f"{s.name:<10} :: {s.id:<7} --> GRADE: {s.average_grade:<3} - MARK: {s.average_mark:>5.2f}" for s in passed
        )
        print(f"\tPASS --> [{pass_line}]")


