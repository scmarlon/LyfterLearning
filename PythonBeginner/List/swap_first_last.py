# Exercise 3: Modify the list by switching the first element with the last element.
print("Exercise 3: Switching the first element with the last element.")
list_example = [9,1,2,3,4,5,6,7,8]
print (f"\nOriginal list: {list_example}")
aux_number = list_example[0] #Replace the first element of the list with the last element, and print the modified list.
list_example[0] = list_example[len(list_example) - 1] #Replace the first element of the list with the last element
list_example[len(list_example) - 1]= aux_number #Replace the last element of the list with the auxiliary number

print(f"Modified list: {list_example}\n") 