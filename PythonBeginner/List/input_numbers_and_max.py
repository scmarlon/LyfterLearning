# Exercise 5: Ask the user to input 10 numbers, and store them in a list. Then, print the list of numbers, and also print the highest number.
print("Exercise 5: Input 10 numbers, print the list of numbers, and the highest number.")
user_numbers = []

for i in range(10): #Ask the user to input 10 numbers, and store them in a list.
    user_input = int(input(f"Enter number {i + 1}: "))
    user_numbers.append(user_input)
print(f"User numbers: {user_numbers}. The highest number is: {max(user_numbers)}.\n") #Print the list of numbers, and also print the highest