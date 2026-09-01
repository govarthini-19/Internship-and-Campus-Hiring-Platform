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
from students import add_student
from jobs import view_jobs
from applications import apply, view_applications
from helpers import title
def student_menu(user_id):
    while True:
        title("STUDENT DASHBOARD")
        print("1. Create Profile")
        print("2. View Jobs")
        print("3. Apply Job")
        print("4. My Applications")
        print("5. Logout")
        choice = input("Choice: ")
        if choice == "1":
            name = input("Name: ")
            cgpa = float(input("CGPA: "))
            skills = input("Skills: ")
            add_student(user_id, name, cgpa, skills)
        elif choice == "2":
            for job in view_jobs():
                print(job)
        elif choice == "3":
            job_id = int(input("Job ID: "))
            student_id = int(input("Student ID: "))
            apply(student_id, job_id)
        elif choice == "4":
            student_id = int(input("Student ID: "))
            for app in view_applications(student_id):
                print(app)
        elif choice == "5":
            break
def company_menu(user_id):
    while True:
        title("COMPANY DASHBOARD")
        print("1. Create Company")
        print("2. Post Job")
        print("3. View Jobs")
        print("4. Shortlist Candidates")
        print("5. Logout")
        choice = input("Choice: ")
        if choice == "1":
            name = input("Company Name: ")
            add_company(user_id, name)
        elif choice == "2":
            company_id = int(input("Company ID: "))
            role = input("Job Role: ")
            skills = input("Required Skills: ")
            cgpa = float(input("Minimum CGPA: "))
            openings = int(input("Openings: "))
            add_job(company_id, role, skills, cgpa, openings)
        elif choice == "3":
            for job in view_jobs():
                print(job)
        elif choice == "4":
            job_id = int(input("Job ID: "))
            shortlist(job_id)
        elif choice == "5":
            break
