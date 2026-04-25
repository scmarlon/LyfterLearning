import re
student_list = [{'name': 'Marlon Sanchez', 'group': '11B', 'grades': {'spanish': 100, 'english': 20, 'science': 89, 'social_studies': 90}},
                {'name': 'Mariana Bri', 'group': '11B', 'grades': {'spanish': 90, 'english': 80, 'science': 66, 'social_studies': 70}},
                {'name': 'Test Student', 'group': '11B', 'grades': {'spanish': 92, 'english': 55, 'science': 78, 'social_studies': 71}},
                {'name': 'Test Student 2', 'group': '11B', 'grades': {'spanish': 80, 'english': 90, 'science': 85, 'social_studies': 88}}]
def validate_grade(course_name):
    try:
        grade = int(input(f"{course_name}"))
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            return validate_grade(course_name)
        return grade
    except ValueError:
        print("Invalid grade. Please enter a valid integer.")
        return validate_grade(course_name)
    
def is_valid_name():
    try:
        name = name = input("Full Name: ")
        if not name.strip():
            print("Name cannot be empty.")
            return is_valid_name()
        if any(char.isdigit() for char in name):
            print("Name cannot contain numbers.")
            return is_valid_name()
        return name
    except ValueError:
        print("Invalid name. Please enter a valid name.")
        return is_valid_name()

def is_valid_group():
    try:
        group = input("Group: ")
        if not group.strip():
            print("Group cannot be empty.")
            return is_valid_group()
        if not re.fullmatch(r'(1[0-2]|[1-9])[A-Z]+', group):
            print("The group must be in format 10A, 11B, etc.")
            return is_valid_group()
        return group
    except ValueError:
        print("Invalid group. Please enter a valid group.")
        return is_valid_group()

def student_exists(name, group):
    for student in student_list:
        if student['name'].lower() == name.lower() and student['group'].lower() == group.lower():
            print(f"Student {name} from group {group} already exists. Please enter a different student.\n")
            return True
    return False

def add_student():
    print("Please complete the information of the student.\n")
    
    while True:
        bool = False
        grade_list = {}
        student_info = {}
        try:
            name = is_valid_name()
            group = is_valid_group()

            if student_exists(name, group):
                return add_student()

            spanish_grade = validate_grade("Spanish Grade: ")
            grade_list["spanish"] = spanish_grade

            english_grade = validate_grade("English Grade: ")
            grade_list["english"] = english_grade

            science_grade = validate_grade("Science Grade: ")
            grade_list["science"] = science_grade

            social_studies_grade = validate_grade("Social Studies Grade: ")
            grade_list["social_studies"] = social_studies_grade

            student_info["name"] = name
            student_info["group"] = group
            student_info["grades"] = grade_list
            
            student_list.append(student_info)
            print(f"Student {name} has been added successfully.")
            while True:
                try:
                    forward = input("Do you want to add another student? (yes/no): ")
                    if forward.lower() == "yes":
                        break
                    elif forward.lower() == "no":
                        print("Student information has been saved.")
                        bool = True
                        break 
                    elif forward.lower() not in ["yes", "no"]:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                except ValueError:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            if bool:
                return student_list
        except ValueError:
            print("Invalid input. Please enter the correct information.")
            continue
#add_student()
def view_students():
    print("View all Students")
    for student in student_list:
        print(f"Name: {student['name']}, Group: {student['group']}")

def average(student):
    grades = student["grades"].values()
    return sum(grades) / len(grades)

def top_students():
    print("Top 3 Students")
    sorted_students = sorted(student_list, key=average, reverse=True)
    for student in sorted_students[:3]:
        print(f"Name: {student['name']}, Group: {student['group']}, Average Grade: {average(student):.2f}")

def average_each_student():
    print("Average grade of each student")
    for student in student_list:
        print(f"Name: {student['name']}, Average Grade: {average(student):.2f}")

def delete_student():
    print("Delete a Student by Name and Group")
    while True:
        try:
            name = input("Enter the full name of the student to delete: ")
            group = input("Enter the group of the student to delete: ")
            student_to_delete = None
            for student in student_list:
                if student['name'].lower() == name.lower() and student['group'].lower() == group.lower():
                    student_to_delete = student
                    break
            if student_to_delete:
                print(f"Are you sure you want to delete {student_to_delete['name']} from group {student_to_delete['group']}? (yes/no)")
                while True:
                    confirm = input().lower()
                    if confirm == "yes":
                        student_list.remove(student_to_delete)
                        print(f"Student {name} from group {group} has been deleted.")
                        print("list ---: ", student_list)
                        break
                    elif confirm == "no":
                        print("Deletion cancelled.")
                        break
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                break
            else:
                print("Student not found. Please check the name and group and try again.")
        except ValueError:
            print("Invalid input. Please enter the correct information.")
            continue
