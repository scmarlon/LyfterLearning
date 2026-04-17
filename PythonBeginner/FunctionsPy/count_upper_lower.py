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