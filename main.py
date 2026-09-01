from db import create_tables
from users import register, login
from helpers import title, get_role
from student_menu import student_menu
from company_menu import company_menu
create_tables()
def register_menu():
    title("REGISTER")
    username = input("Username: ")
    password = input("Password: ")
    role = get_role()
    register(username, password, role)
def main():
    while True:
        title("INTERNSHIP & CAMPUS HIRING PLATFORM")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
       choice = input("Choice: ")
        if choice == "1":
            register_menu()
        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            user = login(username, password)
            if user:
                print("Login successful!")
                if user[1] == "student":
                    student_menu(user[0])
                elif user[1] == "company":
                    company_menu(user[0])
            else:
                print("Invalid login!")
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


main()
