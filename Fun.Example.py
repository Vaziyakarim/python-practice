students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    students.append({"name": name, "age": age, "grade": grade})
    print(f"{name} added successfully!\n")

def display_students():
    if not students:
        print("No students found.\n")
        return
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    print()

def search_student():
    name = input("Enter name to search: ")
    for student in students:
        if student['name'].lower() == name.lower():
            print(f"Found: Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}\n")
            return
    print(f"No student named {name} found.\n")

def update_student():
    name = input("Enter student name to update: ")
    for student in students:
        if student['name'].lower() == name.lower():
            student['name'] = input("Enter new name: ")
            student['age'] = int(input("Enter new age: "))
            student['grade'] = input("Enter new grade: ")
            print("Updated successfully!\n")
            return
    print(f"No student named {name} found.\n")

def delete_student():
    name = input("Enter student name to delete: ")
    for student in students:
        if student['name'].lower() == name.lower():
            students.remove(student)
            print(f"{name} deleted successfully!\n")
            return
    print(f"No student named {name} found.\n")

def main_menu():
    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")

main_menu()
