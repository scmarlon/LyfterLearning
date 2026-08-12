#Function decorator to show all arguments passed to the function
def show_parameters(func):
    def wrapper(*args, ):
        # This will print the arguments and the result
        print(f"Arguments passed to the function: {args}")
        result = func(*args)
        print(f"Result of the function: {result}")
        return result
    return wrapper

@show_parameters
def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result

@show_parameters
def phrase_words(*args):
    phrase = " ".join(args)
    return phrase

#Example usage of the decorator
multiply_args = multiply_numbers(2, 3, 4, 5)

phrase_args = phrase_words("Hello", "world", "!")