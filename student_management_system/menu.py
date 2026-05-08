from actions import *
from data import *

def display_menu():
    # If you want to test the functions with pre-filled data, you can uncomment the following list of students.
    # student_list = [{'name': 'Marlon Sanchez', 'group': '11B', 'grades': {'spanish': 10, 'english': 20, 'science': 89, 'social_studies': 90}},
    #             {'name': 'Mariana Bri', 'group': '11B', 'grades': {'spanish': 90, 'english': 80, 'science': 66, 'social_studies': 70}},
    #             {'name': 'Test Student', 'group': '11B', 'grades': {'spanish': 92, 'english': 55, 'science': 78, 'social_studies': 71}},
    #             {'name': 'Test Test', 'group': '11B', 'grades': {'spanish': 80, 'english': 90, 'science': 85, 'social_studies': 88}}]
    student_list = []
    print("\nWelcome to the Student Management System!\nPlease select an option... \n")
    while True:
        try:
                option = int(input("\n1. Add Student\n2. View Students\n3. Top 3 Students\n4. Average Grades\n5. Delete Student\n6. Students who failed\n7. Export students to CSV\n8. Import students from CSV\n9. Exit\n"))
                if option == 1:
                    add_student(student_list)
                elif option == 2:
                    view_students(student_list)
                elif option == 3:
                    top_students(student_list)
                elif option == 4:
                    average_each_student(student_list)
                elif option == 5:
                    delete_student(student_list)
                elif option == 6:
                    student_failed(student_list)
                elif option == 7:
                    export_data_CSV(student_list)
                elif option == 8:
                    import_data_CSV(student_list)
                elif option == 9:
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    print("Invalid option. Please select a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
