# Exercise 2: Create a function that modifies a global variable. Call the function and print the modified global variable.
print("2: A function that modifies a global variable.")
global_variable = "This is a global variable"
print(f"Global variable: {global_variable}")
def test_function():
    local_variable = "This is a test function" # This variable is local to the function and cannot be accessed outside of it
    global global_variable # This will allow us to modify the global variable inside the function (with global keyword)
    global_variable = "This is a modified global variable"
    return global_variable

test_function() # This will call the function and assign the returned value to the global variable
#print(f"Local variable: {local_variable}") # This will raise an error because local_variable is not defined outside the function
print(f"Modified global variable: {global_variable}\n ------------------------------")