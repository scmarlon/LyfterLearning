#Exercise 3: Create a function that takes a list of numbers as an argument and returns the sum of those numbers.
print("3:A function that takes a list of numbers as an argument and returns the sum of those numbers.")
def sum_numbers_function(list):
    total = 0
    for n in list:
        total += n
    return total

list_of_numbers = [4, 6, 2, 29]
result = sum_numbers_function(list_of_numbers) # This will call the function and pass a list of numbers as an argument, and assign the returned value to the variable result
print(f"The sum of the numbers {list_of_numbers} is: {result}")