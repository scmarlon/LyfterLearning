# This is the main entry point of the student management system. It imports the display_menu function from the menu module and calls it to start the application.
def main():
    from menu import display_menu
    display_menu()

if __name__ == "__main__":
    main()