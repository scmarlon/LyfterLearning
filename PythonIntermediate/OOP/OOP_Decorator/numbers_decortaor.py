#function decorator to verify if all arguments are numbers
def verify_numbers(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"Argument {arg} is not a number.")
        return func(*args, )
    return wrapper


@verify_numbers
def age_employees(*args):
    total_age = sum(args)
    average_age = total_age / len(args)
    return average_age

@verify_numbers
def sum_numbers(*args):
    return sum(args)

list_of_ages = [25, 30, 35, 40,]
list_of_numbers = [10, 20, 30, "20"]
try:
    average_age = age_employees(*list_of_ages)
    print(f"Average age of employees: {average_age}")
except ValueError as e:
    print(e)

try:
    total_sum = sum_numbers(*list_of_numbers)
    print(f"Total sum of numbers: {total_sum}")
except ValueError as e:
    print(e)  # This will raise a ValueError since "20" is not a number
