# Exercise 4: Create a new list that contains only the even numbers from the original list.
print("Exercise 4: List that contains only the even numbers from the original list.")
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 
even_numbers = [] 

print(f"Original list: {number_list}")
for i in range(len(number_list)):
    if number_list[i] % 2 == 0: #Loop through the indices of the list, and print only the even numbers.
        even_numbers.append(number_list[i])

print(f"Even numbers: {even_numbers}\n")