from controller.admin_controller import AdminController
from controller.student_controller import StudentController
from model.database import Database
from colorama import Fore, init, Style

init(autoreset=True)

def main():

    db = Database()

    while True:
        try:
            choice = input(Fore.BLUE + "University System: (A)dmin, (S)tudent, or X: "+ Style.RESET_ALL).upper()

            match choice:
                case "A":
                    admin_controller = AdminController(db)
                    admin_controller.menu()
                case "S":
                    student_controller = StudentController(db)
                    student_controller.menu()
                case "X":
                    print(Fore.YELLOW + "Thank You")
                    break
                case _:
                    print(Fore.YELLOW + "(A) Admin")
                    print(Fore.YELLOW + "(S) Student")
                    print(Fore.YELLOW + "(X) Exit")

        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n\tInterrupted by user")
            break
        except Exception as e:
            print(Fore.YELLOW + f"\tUnexpected error: {e}")

if __name__ == "__main__":
    main()