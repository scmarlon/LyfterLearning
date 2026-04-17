#Exercise 6: Create a function that takes a string and sorts the words in alphabetical order.
print("6: A function that takes a string and sorts the words in alphabetical order.")
unsorted_string = "python-variable-funcion-computadora-monitor"
def sort_string_function(unsorted_string):
    string_list = unsorted_string.split("-") # This will split the string into a list of words using the split() method. The delimiter is the hyphen character.
    sorted_string_list = sorted(string_list) # This will sort the list of words
    sorted_string = "-".join(sorted_string_list) # This will join the sorted list of words into a string using the join() method. The delimiter is the hyphen character.
    return sorted_string

sorted_string = sort_string_function(unsorted_string)
print(f"The original string is: {unsorted_string}")
print(f"The sorted string is: {sorted_string}")