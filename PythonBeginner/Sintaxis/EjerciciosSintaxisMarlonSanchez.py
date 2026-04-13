import random

# string + string → ?
# string + int → ?
# int + string → ?
# list + list → ?
# string + list → ?
# float + int → ?
# bool + bool → ?

print("Hola " + "Marlon")  # string + string → Hola Marlon
print("Hola " + str(5))  # string + int → Hola 5/ without str() would raise an error  
print(str(5) + " Hola")  # int + string → 5 Hola / without str() would raise an error
print([1, 2] + [3, 4])  # list + list
print("Hola " + str([1, 2]))  # string + list → Hola [1, 2] / without str() would raise an error
print(3.14 + 5)  # float + int → 8.14
print(True + False)  # bool + bool → 1 (True is treated as 1 and False as 0 in arithmetic operations)
print(True + True,"\n ------------------------- \n") # bool + bool → 2 (True is treated as 1 in arithmetic operations, so 1 + 1 = 2)

# Exercise: Classify a person based on their age
name = input("Please enter your name: ")
lastname = input("Please enter your lastname: ")
age = int(input("Please enter your age: "))

if age <= 2:
    print(f"\n{name} {lastname} is a baby.")
elif age <= 10:
    print(f"\n{name} {lastname} is a child.")
elif age <=13:
    print(f"\n{name} {lastname} is a pre-teen.")
elif age <= 19:
    print(f"\n{name} {lastname} is a teenager.")
elif age <=30:
    print(f"\n{name} {lastname} is a young adult.")
elif age <= 65:
    print(f"\n{name} {lastname} is an adult.")
else:
    print(f"\n{name} {lastname} is an elder.")
print("\n ------------------------- \n")

# Exercise: Guess the secret number
secret_number = random.randint(1, 10)
guess = int(input("Guess the secret number between 1 and 10: "))
# The loop continues until the user guesses the secret number.
while secret_number != guess:
    if guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess the secret number between 1 and 10: "))
print("\n Congratulations! You guessed the secret number.", "\n ------------------------- \n")

# Exercise: The program has to find the highest of three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

number_list = [number1, number2, number3]
number_list.sort()
length = len(number_list)
print(f"\n The highest number is: {number_list[length - 1]}") # The highest number is the last element of the sorted list.

print("\n ------------------------- \n")    

list_grade_notes = []
passed_grades = []
failed_grades = []

#Enter the number of notes, and then each note is collected and classified as passed or failed.
number_of_notes = int(input("How many notes do you want to enter? "))
for i in range(number_of_notes):
    note = float(input(f"Enter note {i + 1}: "))
    list_grade_notes.append(note) # Add the note to the list of grade notes with .append() method

for note in list_grade_notes: # Iterate through the list of grade notes and classify each note as passed or failed based on the condition (note >= 70).
    if note >= 70:
        passed_grades.append(note)
    else:
        failed_grades.append(note)

print(f"\n The grades entered are: {list_grade_notes}") 
print(f"\n The passed grades are: {passed_grades}")
print(f"\n The failed grades are: {failed_grades}")                                      # Print the list of grade notes with 2 decimal places using string formatting.
print(f"\n The average grade is: {(sum(list_grade_notes) / len(list_grade_notes)):.2f}") # Calculate the average grade by summing all the grades in the list and dividing by the number of grades (length of the list).
print(f"\n The average of the passed grades is: {(sum(passed_grades) / len(passed_grades) if passed_grades else 0):.2f}") #if passed_grades is not empty, calculate the average of the passed grades; otherwise, return 0 to avoid division by zero.
print(f"\n The average of the failed grades is: {(sum(failed_grades) / len(failed_grades) if failed_grades else 0):.2f}")

#same exercise but with a random numbers for list_grade_notes
print("\n ------------------------- \n")

list_grade_notes_random = []
passed_grades_random = []
failed_grades_random = []

for i in range(number_of_notes):
    note_random = random.randint(1, 100)  # Generate a random float between 1 and 100
    list_grade_notes_random.append(note_random)

for note in list_grade_notes_random:
    if note >= 70:
        passed_grades_random.append(note)
    else:
        failed_grades_random.append(note)

print(f"\n The random grades are: {list_grade_notes_random}")
print(f"\n The passed grades are: {passed_grades_random}")
print(f"\n The failed grades are: {failed_grades_random}")
print(f"\n The average grade is: {(sum(list_grade_notes_random) / len(list_grade_notes_random)):.2f}")
print(f"\n The average of the passed grades is: {(sum(passed_grades_random) / len(passed_grades_random) if passed_grades_random else 0):.2f}")
print(f"\n The average of the failed grades is: {(sum(failed_grades_random) / len(failed_grades_random) if failed_grades_random else 0):.2f}")