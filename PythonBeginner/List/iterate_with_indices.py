# Exercise 1: Iterating with indices
print("\nExercise 1: Iterating with indices")
first_list  = ["Hay", "en", "que", "iteracion", "indices", "muy" ]
second_list =["casos", "los", "la", "por", "es", "util"]

for i in range(len(first_list)): #Loop through the indices of the lists, and print the corresponding elements from both lists.
    print(f"{first_list[i]} {second_list[i]}")