#Exercise 2: Create a dictionary from two lists
print("\n2. Create a dictionary from two lists")
list_a = ["first_name", "last_name", "role"]
list_b = ["Marlon", "Sanchez", "Software Engineer"]

dictionary = {}

for i in range(len(list_a)):
    dictionary[list_a[i]] = list_b[i]

print(dictionary) 