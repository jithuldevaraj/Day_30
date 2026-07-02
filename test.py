try:
    # Trying to open a file that doesn't exist
    with open("ghost_file.txt", "r") as file:
        content = file.read()

except FileNotFoundError as error:
    # We caught the Exception Object and named it 'e'
    print("Uh oh, something went wrong.")

    # Now we can print the exact error message Python generated!
    print(f"The exact error was: {error}")