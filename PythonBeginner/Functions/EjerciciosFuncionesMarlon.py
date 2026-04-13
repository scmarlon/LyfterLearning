# Exercise 1: Create two functions that print different messages. Call the first function, which should then call the second function. 
print("\n1:Two functions that print different messages. Call the first function, which should then call the second function.")
def first_function():
    print("This is the first function")
    second_function()


def second_function():
    print("This is the second function\n ------------------------------")

first_function()

# Exercise 2: Create a function that modifies a global variable. Call the function and print the modified global variable.
print("2: A function that modifies a global variable.")
global_variable = "This is a global variable"
print(f"Global variable: {global_variable}")
def test_function():
    local_variable = "This is a test function" # This variable is local to the function and cannot be accessed outside of it
    global global_variable # This will allow us to modify the global variable inside the function (with global keyword)
    global_variable = "This is a modified global variable"
    return global_variable

test_function() # This will call the function and assign the returned value to the global variable
#print(f"Local variable: {local_variable}") # This will raise an error because local_variable is not defined outside the function
print(f"Modified global variable: {global_variable}\n ------------------------------")

#Exercise 3: Create a function that takes a list of numbers as an argument and returns the sum of those numbers.
print("3:A function that takes a list of numbers as an argument and returns the sum of those numbers.")
def sum_numbers_function(list):
    total = 0
    for n in list:
        total += n
    return total

list_of_numbers = [4, 6, 2, 29]
result = sum_numbers_function(list_of_numbers) # This will call the function and pass a list of numbers as an argument, and assign the returned value to the variable result
print(f"The sum of the numbers {list_of_numbers} is: {result}\n ------------------------------")

#Exercise 4: Create a function that takes a string and returns the string in reverse order.
print("4: A function that takes a string and returns the string in reverse order.")
def reverse_string_function(string_default):
    aux_string = ""
    print(f"The default string is: {string_default}")
    #reversed_string = string_default[::-1] # This will reverse the string using slicing. Easy way to reverse a string in Python.
    for i in range(len(string_default) -1, -1, -1): # This will reverse the string using a for loop. It will iterate through the string in reverse order and concatenate the characters.
        aux_string += string_default[i]
    print(f"The reversed string is: {aux_string}\n ------------------------------")
    return aux_string

string_default= "Hello World"
reverse_string_function(string_default)

# Exercise 5: Create a function that takes a string and counts the number of uppercase and lowercase letters
print("5: A function that counts the number of uppercase and lowercase letters in a string.")
def number_upper_and_lower_function(string):
    upper_counter = 0
    lower_counter = 0
    print(f"The string is: {string}")
    for i in range(len(string)):
        if string[i].isupper(): # This will check if the character is an uppercase letter using the isupper() method. If it is, it will increment the upper_counter variable by 1.
            upper_counter += 1
        elif string[i].islower():
            lower_counter += 1
    print(f"There´s {upper_counter} uppercase letters and {lower_counter} lowercase letters in the string.\n ------------------------------")

string = "I love Nation Sushi"
number_upper_and_lower_function(string)

#Exercise 6: Create a function that takes a string and sorts the words in alphabetical order.
print("6: A function that takes a string and sorts the words in alphabetical order.")
unsorted_string = "python-variable-funcion-computadora-monitor"
def sort_string_function(unsorted_string):
    string_list = unsorted_string.split("-") # This will split the string into a list of words using the split() method. The delimiter is the hyphen character.
    sorted_string_list = sorted(string_list) # This will sort the list of words
    sorted_string = "-".join(sorted_string_list) # This will join the sorted list of words into a string using the join() method. The delimiter is the hyphen character.
    return sorted_string

sorted_string = sort_string_function(unsorted_string)
print(f"The original string is: {unsorted_string}")
print(f"The sorted string is: {sorted_string}\n ------------------------------")

#Exercise 7: Create a function that takes a list of numbers and returns a list of the prime numbers in the original list.
print("7: A function that takes a list of numbers and returns a list of the prime numbers")
def list_numbers_function(numbers_list):
    prime_numbers = []
    for number in numbers_list:
        if number > 1: # This will check if the number is greater than 1, because prime numbers are greater than 1
            for i in range(2, number): # This will check if the number is divisible by any number between 2 and n-1. If it is, it is not a prime number.
                if number % i == 0:
                    break
            else: # This will execute if the loop completes without finding a divisor, which means the number is prime.
                prime_numbers.append(number) # This will add the prime number to the list of prime numbers.  
    return prime_numbers


numbers_list = [1, 4, 6, 7, 13, 9, 67]
result = list_numbers_function(numbers_list)
print(f"The original list of numbers is: {numbers_list}")
print(f"The prime numbers in the list are: {result}\n")