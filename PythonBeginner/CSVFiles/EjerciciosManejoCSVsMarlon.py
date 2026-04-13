import csv
# This program allows the user to input information about video games and saves it in a CSV file.
def create_csv(games_list):
    with open("video_games.csv", "w") as file:
        write = csv.DictWriter(file, games_list[0].keys()) # The keys of the first dictionary in the list are used as the header of the CSV file.
        write.writeheader() # Writes the header to the CSV file.
        write.writerows(games_list) # Writes the rows of the CSV file using the list of dictionaries. Each dictionary represents a row in the CSV file.
    print("CSV file created successfully!")

    with open("video_gamesV2.csv", "w") as file:
        write = csv.DictWriter(file, games_list[0].keys(), delimiter="\t") # The keys of the first dictionary in the list are used as the header of the CSV file. The delimiter is set to a tab character.
        write.writeheader()
        write.writerows(games_list)
    print("CSV file with tab delimiter created successfully!")
    exit()

#  The main menu function allows the user to input information about video games and saves it in a list of dictionaries. Each dictionary represents a video game with its attributes.
def main_menu():
    print("Welcome to the CSV Management Program!\n")
    games_list = []
    while True:
        dictionary_games = {}
        try:
            name = input("Enter the name of the video game: ")
            gender = input("Enter the gender of the video game: ")
            developer = input("Enter the developer of the video game: ")
            esrb_rating = input("Enter the ESRB rating of the video game: ")
            dictionary_games["Name"] = name
            dictionary_games["Gender"] = gender
            dictionary_games["Developer"] = developer
            dictionary_games["ESRB Rating"] = esrb_rating
            games_list.append(dictionary_games)
            print(games_list)
            while True:
                try:
                    forward = input("Do you want to add another video game? (yes/no): ")
                    if forward.lower() == "yes":
                        break
                    elif forward.lower() == "no":
                        create_csv(games_list)
                    elif forward.lower() not in ["yes", "no"]:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                except ValueError:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        except Exception as e: # Catches any exception that may occur during the input process and prints an error message.
            print(f"An error occurred: {e}")
            return

if __name__ == "__main__": # This condition checks if the script is being run directly (as the main program) rather than imported as a module. If it is being run directly, it calls the main_menu() function to start the program.
    main_menu()