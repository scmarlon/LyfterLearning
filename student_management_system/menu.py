def menu():
    print("\nWelcome to the Student Management System!\nPlease select an option... \n")
    while True:
        try:
                option = int(input("\n1. Add Student\n2. View Students\n3. Top 3 Students\n4. Average Grades\n5. Delete Student\n8. Exit\n"))
                if option == 1:
                    from actions import add_student
                    add_student()
                elif option == 2:
                    from actions import view_students
                    view_students()
                elif option == 3:
                    from actions import top_students
                    top_students()
                elif option == 4:
                    from actions import average_each_student
                    average_each_student()
                elif option == 5:
                    from actions import delete_student
                    delete_student()
                elif option == 8:
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    print("Invalid option. Please select a number between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")

menu()