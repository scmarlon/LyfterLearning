
# This is a calculator that allows the user to perform basic arithmetic operations (addition, subtraction, multiplication, and division) on a global number. The program handles exceptions such as invalid input and division by zero, and it provides error messages to guide the user in case of invalid operations.
def __main__():
    default_number = 50
    while True: # This is the main loop of the program, it will continue to run until the user decides to exit the program.
        print(f"\nWelcome to Calculator.\n"
        f"Select one of the following options:\n"
        f"1. Addition\n"
        f"2. Subtraction\n"
        f"3. Multiplication\n"
        f"4. Division\n"
        f"5. Eraser the actual number.\n"
        f"6. Exit the program.\n")
        print(f"Current number: {default_number}\n")
        try: # This try block is used to catch any ValueError that may occur when the user enters an invalid input, such as a string or a float, which is not allowed in this case.
            option = int(input("Select one option: "))
            if option == 1:
                default_number = addition_function(default_number) #Call the addition function and pass the default_number, update default_number after the operation is performed.
            elif option == 2:
                default_number = subtraction_function(default_number) #Same as above but for subtraction.
            elif option == 3:
                default_number = multiplication_function(default_number)
            elif option == 4:
                default_number = division_function(default_number)
            elif option == 5:
                default_number = eraser_function(default_number)
            elif option == 6:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid option. Please select a valid option.")
        except ValueError as e: #ValueError is raised when the user enters an invalid input, such as a string or a float. 
            print(f"Invalid input. Please enter a valid number. Error: {e}") #This will print an error message to the user, indicating that the input was invalid.

#addition_function allows the user to add a number to the default number. 
def addition_function(default_number):
    try:# This try block is used to catch any ValueError that may occur when the user enters an invalid input
        print("Enter the number you want to add")
        add_number = int(input(f"{default_number} + "))
        result = default_number + add_number # This is the actual addition operation, it adds the global number.
        default_number = result
        print(f"The result of the addition is: {result}")
        return default_number # This return the new value of the global number after the addition operation is performed.
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return addition_function(default_number)

#subtraction_function allows the user to subtract a number from the default number. It also handles exceptions such as invalid input and provides error messages to guide the user in case of invalid operations.
def subtraction_function(default_number):
    print("Enter the number you want to subtract")
    try:
        sub_number = int(input(f"{default_number} - "))
        result = default_number - sub_number
        default_number = result
        print(f"The result of the subtraction is: {result}")
        return default_number
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return subtraction_function(default_number)

#multiplication_function allows the user to multiply the default number by another number. It also handles exceptions.
def multiplication_function(default_number):
    print("Enter the number you want to multiply")
    try:
        mult_number = int(input(f"{default_number} * "))
        result = default_number * mult_number
        default_number = result
        print(f"The result of the multiplication is: {result}")
        return default_number
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return multiplication_function(default_number)

#division_function allows the user to divide the default number by another number. It also handles exceptions.
def division_function(default_number):
    print("Enter the number you want to divide")
    try:# This try block is used to catch a division by zero error, which occurs when the user tries to divide the default number by zero.
        div_number = int(input(f"{default_number} / "))
        try:
            result = round(default_number / div_number, 2)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return division_function(default_number)
        result = round(default_number / div_number, 2)
        default_number = result
        print(f"The result of the division is: {result}")
        return default_number
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return division_function(default_number) 

#eraser_function allows the user to reset the default number to zero.
def eraser_function(default_number):
    print("The actual number has been erased.")
    default_number = 0
    return default_number 


__main__()