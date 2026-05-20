from actions import add_student, view_students, top_students, average_each_student, delete_student, student_failed
from data import export_data_CSV, import_data_CSV

def display_menu():
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
