import re

class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

# Function to validate name input and ensure it's not empty and doesn't contain numbers
def is_valid_name():
        while True:
            name = input("Full Name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            if any(char.isdigit() for char in name):
                print("Name cannot contain numbers.")
                continue
            return name

# Function to validate group input and ensure it's not empty and follows the format of a number followed by uppercase letters (e.g., 1A, 8B, 12C)
def is_valid_group():
    while True:
        group = input("Group: ").strip()
        if not group:
            print("Group cannot be empty.")
            continue
        if not re.fullmatch(r'(1[0-2]|[1-9])[A-Z]+', group): #re library to validate the group format, use fullmatch to ensure the entire string matches the pattern
            print("The group must be in format 1A, 8B, 12C etc.")
            continue
        return group
    
# Function to validate grade input and ensure it's between 0 and 100
def validate_grade(course_name):
    while True:
        try:
            grade = int(input(f"Enter the grade for {course_name}: "))
            if 0 <= grade <= 100:
                return grade
            print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid grade. Please enter a valid integer.")

# Function to check if a student with the same name and group already exists in the student list
def student_exists(name, group, student_list, check_coming):
    if not student_list or student_list == []:
        return False
    for student in student_list:
        if student.name.lower() == name.lower() and student.group.lower() == group.lower():
            if not check_coming:
                print(f"Student {name} from group {group} already exists. Please enter a different student.\n")
            return True
    return False

# Function to add a student to the student list, including validation for name, group, and grades
def add_student(student_list):
    print("Please complete the information of the student.\n")
    while True:
        continue_loop  = False
        name = is_valid_name()
        group = is_valid_group()

        if student_exists(name, group, student_list, check_coming=False):
            continue

        spanish_grade = validate_grade("Spanish")
        english_grade = validate_grade("English")
        science_grade = validate_grade("Science")
        social_studies_grade = validate_grade("Social Studies")

        student = Student(
            name,
            group,
            {
                "spanish": spanish_grade,
                "english": english_grade,
                "science": science_grade,
                "social_studies": social_studies_grade
            }
        )
        student_list.append(student)
        print(f"\nStudent {name} from group {group} has been added successfully.\n")

        #The following loop asks the user if they want to add another student after successfully adding one.
        while True:
            forward = input("Do you want to add another student? (yes/no): ")
            if forward.lower() == "yes":
                break
            elif forward.lower() == "no":
                print("Student information has been saved.")
                continue_loop  = True
                break 
            elif forward.lower() not in ["yes", "no"]:
                print("Invalid input. Please enter 'yes' or 'no'.")  
        if continue_loop :
            return student_list

# Function to view all students in the student list, displaying their name and group
def view_students(student_list):
    if not student_list or student_list == []:
        print("No students to display.")
        return
    try:
        for student in student_list:
            print(f"\nName: {student.name}")
            print(f"Group: {student.group}")
            print("Grades:")
            for course, grade in student.grades.items():
                print(f" - {course.capitalize()}: {grade}")
            print("-" * 30)
    except KeyError:
        print("Error: One or more students do not have the required keys (name, group).")

# Function to display the top 3 students based on their average grades, showing their name, group, and average grade.
def top_students(student_list):
    if not student_list or student_list == []:
        print("No students to evaluate.")
        return
    try:
        sorted_students = sorted(student_list, key=lambda s: sum(s.grades.values()) / len(s.grades), reverse=True)
        top_3 = sorted_students[:3]
        print("\nTop 3 Students:")
        for student in top_3:
            average_grade = sum(student.grades.values()) / len(student.grades)
            print(f"Name: {student.name}, Group: {student.group}, Average Grade: {average_grade:.2f}")
    except KeyError:
        print("Error: One or more students do not have the required keys (name, group, grades).")

# Function to calculate and display the average grade of each student, showing their name and average grade.
def average_each_student(student_list):
    if not student_list or student_list == []:
        print("No students to evaluate.")
        return
    try:
        print("\nAverage Grades for Each Student:")
        for student in student_list:
            average_grade = sum(student.grades.values()) / len(student.grades)
            print(f"Name: {student.name}, Average Grade: {average_grade:.2f}")
    except KeyError:
        print("Error: One or more students do not have the required keys (name, grades).")

# Function to delete a student from the student list based on their name and group, with confirmation before deletion.
def delete_student(student_list):
    if not student_list or student_list == []:
        print("No students to delete.")
        return
    print("Delete a Student by Name and Group")
    while True:
        try:
            name = input("Enter the name of the student to delete: ").strip()
            group = input("Enter the group of the student to delete: ").strip()
            student_to_delete = None
            for student in student_list:
                if student.name.lower() == name.lower() and student.group.lower() == group.lower():
                    student_to_delete = student
                    break
            if student_to_delete:
                confirmation = input(f"Are you sure you want to delete {student_to_delete.name} from group {student_to_delete.group}? (yes/no): ")
                if confirmation.lower() == "yes":
                    student_list.remove(student_to_delete)
                    print(f"Student {student_to_delete.name} from group {student_to_delete.group} has been deleted.")
                    return
                else:
                    print("Deletion cancelled.")
                    return
            print(f"No student found with name {name} and group {group}.")
        except ValueError:
            print("Invalid input. Please enter the correct information.")
            continue

# Function to display students who have failed at least one course, showing their name, group, and the courses they failed along with the grades.
def student_failed(student_list):
    if not student_list or student_list == []:
        print("No students to evaluate.")
        return
    print("\nStudents Who Failed at Least One Course:")
    try:
        for student in student_list:
            failed_courses = {
                course: grade
                for course, grade in student.grades.items() 
                if grade < 60
                }
            if not failed_courses:
                continue

            print(f"Name: {student.name}, Group: {student.group}")
            print("Failed Courses:")
            for course, grade in failed_courses.items():
                print(f" - {course.capitalize()}: {grade}")
            print("-" * 30)
    except KeyError:
        print("Error: One or more students do not have the required keys (name, group, grades).")