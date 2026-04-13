#Exercise 1: Create a dictionary with Hotel information
print("\n1. Create a dictionary with Hotel information")
hotel_dictionary= {
    "name": "Dodgers ",
    "stars_number": 4,
    "rooms":[{
        "room_number": 101,
        "floor_number": 1,
        "price_per_night": 150
    }, {
        "room_number": 102,
        "floor_number": 1,
        "price_per_night": 200
    },
    {
        "room_number": 201,
        "floor_number": 2,
        "price_per_night": 155
    }]
    }

print(f"{hotel_dictionary['name']}Hotel has {hotel_dictionary['stars_number']} stars, and the following rooms:")
#Loop through the rooms and print their details
for key, value in hotel_dictionary.items():
    if key == "rooms":
        for room in value:
            print(f"  Room number: {room['room_number']}, "
                  f"Floor number: {room['floor_number']}, "
                  f"Price per night: ${room['price_per_night']}")


#Exercise 2: Create a dictionary from two lists
print("\n2. Create a dictionary from two lists")
list_a = ["first_name", "last_name", "role"]
list_b = ["Marlon", "Sanchez", "Software Engineer"]

dictionary = {}

for i in range(len(list_a)):
    dictionary[list_a[i]] = list_b[i]

# dictionary = dict(zip(list_a, list_b)) easy way to create a dictionary from two lists
#dictionary = {list_a[i]: list_b[i] for i in range(len(list_a))}

print(dictionary)   

#Exercise 3: Remove specific keys from a dictionary using keys form another list
print("\n3. Remove specific keys from a dictionary using keys form another list")
keys_list = ["access_level", "age",]
employee = {"name": "Marlon", "mail": "marlon@gmail.com", "access_level": 5, "age": 28}

print("Full Employee data: ", employee)

for key in keys_list:
    employee.pop(key, None)  # Remove the key if it exists, otherwise do nothing

print("Employee data without access level and age: ", employee,"\n")
