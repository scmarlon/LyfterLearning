#Function decorator to show all arguments passed to the function
def show_parameters(func):
    def wrapper(*args, ):
        print(f"Arguments passed to the function: {args}")
        return func(*args)
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

multiply_args = multiply_numbers(2, 3, 4, 5)
print(multiply_args)  # This will print the arguments and the result of multiplication

phrase_args = phrase_words("Hello", "world", "!")
print(phrase_args)  # This will print the arguments and the result of joining the words