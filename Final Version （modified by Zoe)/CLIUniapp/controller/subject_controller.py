from model.subject import Subject
from utils.validate import validate
from colorama import Fore, init, Style

class SubjectController:

    def __init__(self, student, db):
        self.student = student
        self.db = db

    def menu(self):
        while True:
            try:
                choice = input(Fore.BLUE + "\t\tStudent Course Menu (c/e/r/s/x): " + Style.RESET_ALL).lower()

                match choice:
                    case "c":
                        self.change_password()
                    case "e":
                        self.enrol()
                    case "r":
                        self.remove()
                    case "s":
                        self.show()
                    case "x":
                        break
                    case _:
                        print(Fore.YELLOW + "\t\t(c) change: Change the password")
                        print(Fore.YELLOW + "\t\t(e) enrol: Enrol in a subject. A student can enrol in a maximum of four (4) subjects")
                        print(Fore.YELLOW + "\t\t(r) remove: Remove a subject from the enrolment list")
                        print(Fore.YELLOW + "\t\t(s) show: Shows the enrolled subjects with their marks and grades")
                        print(Fore.YELLOW + "\t\t(x) exit")

            except KeyboardInterrupt:
                print(Fore.YELLOW + "\n\tInterrupted by user")
                break
            except Exception as e:
                print(Fore.YELLOW + f"\t\tUnexpected error: {e}")        


    def change_password(self):

        try:
            print(Fore.YELLOW + "\t\tUpdating Password")
            pd_ = input("\t\tNew Password:")

            if validate(self.student.email, pd_):
                while True:
                    if pd_ == input("\t\tConfirm Password:"):
                        self.student.set_password(pd_)
                        self.db.save_students()
                        break
                    else:
                        print(Fore.RED + "\t\tPassword does not match - try again")
            else:
                print(Fore.RED + "\t\tIncorrect password format")

        except Exception as e:
            print(Fore.YELLOW + f"\t\tUnexpected error: {e}")        


    def enrol(self):
        if self.check_max():
            print(Fore.RED + "\t\tStudents are allowed to enrol in 4 subjects only")
            return

        while True:
            new_subject = Subject()
            if self.student.get_subject(new_subject.id) is None:
                self.student.subjects.append(new_subject)
                self.db.save_students()
                print(Fore.YELLOW + f"\t\tEnrolling in Subject - {new_subject.id}")
                print(Fore.YELLOW + f"\t\tYou are now enrolled in {len(self.student.subjects)} subject out of 4 subjects")
                break
            else:
                continue

    def check_max(self):
        return len(self.student.subjects) >= 4

    def remove(self):
        try:
            id_ = input("\t\tRemove subject by id: ")
            del_subject = self.student.get_subject(id_)

            if del_subject is None:
                print(Fore.RED + "\t\tSubject id doesn't exist")
            else:
                self.student.subjects.remove(del_subject)
                self.db.save_students()
                print(Fore.YELLOW + f"\t\tDropping Subject - {id_}")
                print(Fore.YELLOW + f"\t\tYou are now enrolled in {len(self.student.subjects)} subject out of 4 subjects")

        except Exception as e:
            print(Fore.YELLOW + f"\t\tUnexpected error: {e}")        


    def show(self):
        if self.student.subjects:
            print(Fore.YELLOW + f"\t\tShowing {len(self.student.subjects)} subjects:")
            for s in self.student.subjects:
                print(f"\t\t{s}")
        else:
            print(Fore.YELLOW + f"\t\tShowing 0 subjects")
