#Exercise 3: Remove specific keys from a dictionary using keys form another list
print("\n3. Remove specific keys from a dictionary using keys form another list")
keys_list = ["access_level", "age",]
employee = {"name": "Marlon", "mail": "marlon@gmail.com", "access_level": 5, "age": 28}

print("Full Employee data: ", employee)

for key in keys_list:
    employee.pop(key, None)  # Remove the key if it exists, otherwise do nothing

print("Employee data without access level and age: ", employee,"\n")