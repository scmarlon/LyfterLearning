
# string + string → ?
# string + int → ?
# int + string → ?
# list + list → ?
# string + list → ?
# float + int → ?
# bool + bool → ?

print("Hola " + "Marlon")  # string + string → Hola Marlon
print("Hola " + str(5))  # string + int → Hola 5/ without str() would raise an error  
print(str(5) + " Hola")  # int + string → 5 Hola / without str() would raise an error
print([1, 2] + [3, 4])  # list + list
print("Hola " + str([1, 2]))  # string + list → Hola [1, 2] / without str() would raise an error
print(3.14 + 5)  # float + int → 8.14
print(True + False)  # bool + bool → 1 (True is treated as 1 and False as 0 in arithmetic operations)
print(True + True) # bool + bool → 2 (True is treated as 1 in arithmetic operations, so 1 + 1 = 2)