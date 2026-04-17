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