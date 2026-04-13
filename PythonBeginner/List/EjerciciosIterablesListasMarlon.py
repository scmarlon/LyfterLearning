
# Exercise 1: Iterating with indices
print("\nExercise 1: Iterating with indices")
first_list  = ["Hay", "en", "que", "iteracion", "indices", "muy" ]
second_list =["casos", "los", "la", "por", "es", "util"]

for i in range(len(first_list)): #Loop through the indices of the lists, and print the corresponding elements from both lists.
    print(f"{first_list[i]} {second_list[i]}")
print("\n")

#Exercise2: Print elements of the list right to left.
print("Exercise 2: Print elements of the list right to left.")
string_example = "Iterating list is funny"
print(f"Original string: {string_example}")
for i in range(len(string_example)):
    print(string_example[len(string_example) - 1 - i]) #Loop through the indices of the string in reverse order, and print each character.

print("\n")

# Exercise 3: Modify the list by switching the first element with the last element.
print("Exercise 3: Switching the first element with the last element.")
list_example = [9,1,2,3,4,5,6,7,8]
print (f"\nOriginal list: {list_example}")
aux_number = list_example[0] #Replace the first element of the list with the last element, and print the modified list.
list_example[0] = list_example[len(list_example) - 1] #Replace the first element of the list with the last element
list_example[len(list_example) - 1]= aux_number #Replace the last element of the list with the auxiliary number

print(f"Modified list: {list_example}\n") 

# Exercise 4: Create a new list that contains only the even numbers from the original list.
print("Exercise 4: List that contains only the even numbers from the original list.")
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 
even_numbers = [] 

print(f"Original list: {number_list}")
for i in range(len(number_list)):
    if number_list[i] % 2 == 0: #Loop through the indices of the list, and print only the even numbers.
        even_numbers.append(number_list[i])

print(f"Even numbers: {even_numbers}\n")

# Exercise 5: Ask the user to input 10 numbers, and store them in a list. Then, print the list of numbers, and also print the highest number.
print("Exercise 5: Input 10 numbers, print the list of numbers, and the highest number.")
user_numbers = []

for i in range(10): #Ask the user to input 10 numbers, and store them in a list.
    user_input = int(input(f"Enter number {i + 1}: "))
    user_numbers.append(user_input)
print(f"User numbers: {user_numbers}. The highest number is: {max(user_numbers)}.\n") #Print the list of numbers, and also print the highest