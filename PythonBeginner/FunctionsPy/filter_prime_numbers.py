#Exercise 7: Create a function that takes a list of numbers and returns a list of the prime numbers in the original list.
print("7: A function that takes a list of numbers and returns a list of the prime numbers")
def list_numbers_function(numbers_list):
    prime_numbers = []
    for number in numbers_list:
        if number > 1: # This will check if the number is greater than 1, because prime numbers are greater than 1
            for i in range(2, number): # This will check if the number is divisible by any number between 2 and n-1. If it is, it is not a prime number.
                if number % i == 0:
                    break
            else: # This will execute if the loop completes without finding a divisor, which means the number is prime.
                prime_numbers.append(number) # This will add the prime number to the list of prime numbers.  
    return prime_numbers


numbers_list = [1, 4, 6, 7, 13, 9, 67]
result = list_numbers_function(numbers_list)
print(f"The original list of numbers is: {numbers_list}")
print(f"The prime numbers in the list are: {result}\n")