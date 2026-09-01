def line():
    print("-" * 40)

def title(text):
    line()
    print(text)
    line()

def get_role():
    while True:
        role = input("Role (student/company): ").lower()
        if role in ["student", "company"]:
            return role
        print("Enter student or company.")
