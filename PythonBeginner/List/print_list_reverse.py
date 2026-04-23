#Exercise2: Print elements of the list right to left.
print("Exercise 2: Print elements of the list right to left.")
string_example = "Iterating list is funny"
print(f"Original string: {string_example}")
for i in range(len(string_example)):
    print(string_example[len(string_example) - 1 - i]) #Loop through the indices of the string in reverse order, and print each character.