# Exercise 1: Create two functions that print different messages. Call the first function, which should then call the second function. 
print("\n1:Two functions that print different messages. Call the first function, which should then call the second function.")
def first_function():
    print("This is the first function")
    second_function()


def second_function():
    print("This is the second function\n ------------------------------")

first_function()