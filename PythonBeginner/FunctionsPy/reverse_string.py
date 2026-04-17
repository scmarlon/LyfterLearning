#Exercise 4: Create a function that takes a string and returns the string in reverse order.
print("4: A function that takes a string and returns the string in reverse order.")
def reverse_string_function(string_default):
    aux_string = ""
    print(f"The default string is: {string_default}")
    #reversed_string = string_default[::-1] # This will reverse the string using slicing. Easy way to reverse a string in Python.
    for i in range(len(string_default) -1, -1, -1): # This will reverse the string using a for loop. It will iterate through the string in reverse order and concatenate the characters.
        aux_string += string_default[i]
    print(f"The reversed string is: {aux_string}")
    return aux_string

string_default= "Hello World"
reverse_string_function(string_default)