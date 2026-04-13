import json

# Function to write the updated pokemons data back to the JSON file
def write_pokemonsJSON(data):
    try:
        with open("pokemons.json", "w") as file: #Open the pokemons.json file in write mode to update it with the new data
            json.dump(data, file, indent=4) #Use json.dump to write the updated data back to the pokemons.json file with an indentation of 4 for better readability 
            print("Pokemons data has been updated in pokemons.json.")
            return
    except Exception as e:
        print(f"Error writing to pokemons.json: {e}")

# Function to create a new Pokemon and add it to the existing data
def create_pokemon(data):
    print("\nEnter the details of the new Pokemon...\n")
    try:
        name = input("Pokemon Name: ")
        level = int(input("Level: "))
        types = input("type: ")
        hp = int(input("HP: "))
        attack = int(input("Attack: "))
        defense = int(input("Defense: "))
        sp_attack = int(input("Sp. Attack: "))
        sp_defense = int(input("Sp. Defense: "))
        speed = int(input("Speed: "))
    except ValueError:
        print("Error: Invalid input. Please enter the correct data types.")
        return create_pokemon(data)
    
    try:
        new_pokemon = {
        "name": {
        "english": name
        },
        "level": level,
        "type": [types],
        "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed}}
        data.append(new_pokemon)
        return write_pokemonsJSON(data) #Call the write_pokemonsJSON function to save the updated data to the pokemons.json file
    except Exception as e:
        print(f"Error creating new pokemon: {e}")

# Read existing pokemons data from JSON file
def read_pokemonsJSON():
    try:
        with open("pokemons.json", "r") as file: #Open the pokemons.json file in read mode
            data = json.load(file)
            return create_pokemon(data) #Call the create_pokemon function with the loaded data to add a new pokemon
    except FileNotFoundError:
        print("Error: pokemons.json file not found.") #Handle the case where the pokemons.json file does not exist

read_pokemonsJSON()