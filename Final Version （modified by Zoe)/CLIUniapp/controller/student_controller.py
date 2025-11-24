from controller.subject_controller import SubjectController
from model.student import Student
from utils.validate import validate
from colorama import Fore, init, Style

class StudentController:

    def __init__(self, db):
        self.db = db

    def menu(self):
        while True:
            try:

                choice = input(Fore.BLUE + "\tStudent System (l/r/x): " + Style.RESET_ALL).lower()

                match choice:
                    case "l":
                        self.login()
                    case "r":
                        self.register()
                    case "x":
                        break
                    case _:
                        print(Fore.YELLOW + "\t(l) login")
                        print(Fore.YELLOW + "\t(r) register")
                        print(Fore.YELLOW + "\t(x) exit")

            except KeyboardInterrupt:
                print(Fore.YELLOW + "\n\tInterrupted by user")
                break
            except Exception as e:
                print(Fore.YELLOW + f"\tUnexpected error: {e}")        

    def login(self):
        try:
            print(Fore.GREEN + "\tStudent Sign In")

            while True:
                login_id = input("\tEmail: ")
                login_pw = input("\tPassword: ")

                if validate(login_id, login_pw):
                    print(Fore.YELLOW + "\temail and password formats acceptable")
                    std = self.db.get_email(login_id)

                    if std:
                        if std.password == login_pw:
                            SubjectController(std, self.db).menu()
                            break
                        else:
                            print(Fore.RED + "\tIncorrect password")
                    else:
                        print(Fore.RED +"\tStudent does not exist")
                        return
                else:
                    print(Fore.RED +"\tIncorrect email or password format")
        
        except Exception as e:
            print(Fore.YELLOW + f"\tUnexpected error: {e}")        


    def register(self):

        try:
            print(Fore.GREEN + "\tStudent Sign Up")

            while True:
                new_id = input("\tEmail: ")
                new_pw = input("\tPassword: ")

                if validate(new_id, new_pw):
                    print(Fore.YELLOW +"\temail and password formats acceptable")
                else:
                    print(Fore.RED +"\tIncorrect email or password format")
                    continue

                std = self.db.get_email(new_id)
                if std:
                    print(Fore.RED + f"\tStudent {std.name} already exists")
                    return
                break

            new_name = input("\tName: ")
            while True:
                new_student = Student(new_name, new_id, new_pw)
                if self.db.get_id(new_student.id) is None:
                    break

            self.db.add_student(new_student)
            print(Fore.YELLOW +f"\tEnrolling Student {new_name}")

        except Exception as e:
            print(Fore.YELLOW + f"\tUnexpected error: {e}")        

