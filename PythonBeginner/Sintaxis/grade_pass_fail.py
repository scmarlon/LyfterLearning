import random

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