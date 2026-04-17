#This function writes the sorted list of songs to a new file called "new_songs.txt".
def write_file(sorted_songs):
    file_path = "new_songs.txt"
    try:
        with open(file_path, 'w') as file: # This will open the file in write mode using the open() function and the 'w' mode.
            for song_name in sorted_songs:
                file.write(song_name) # This will write each song in the sorted list of songs to the new file using the write() method.
            print(f"Content written to '{file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# This function sorts the list of songs in alphabetical order and then writes the sorted list to a new file.
def sort_songs(list_of_songs):
    try:
        sorted_songs = sorted(list_of_songs) # This will sort the list of songs in alphabetical order using the sorted() function.
        write_file(sorted_songs)
        return sorted_songs
    except Exception as e:
        print(f"An error occurred while sorting the songs: {e}")

# This function reads the file that we gonna use to get the list of songs.
def read_file():
    try:
        list_of_songs = []
        file_path = "songs.txt"
        with open(file_path, 'r') as file: # This will open the file in read mode using the open() function and the 'r' mode.
            for line in file.readlines():
                list_of_songs.append(line) # This will append the list of songs to the list_of_songs variable.
            sort_songs(list_of_songs) # This will sort the list of songs in alphabetical order using the sort_songs() function.
            return list_of_songs
    except FileNotFoundError: # This will catch the FileNotFoundError exception if the file is not found and print an error message.
        print(f"Error: The file '{file_path}' was not found.")

read_file()