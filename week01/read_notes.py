from notes_utils import read_file_reader

print("NOTES READER\n\n")
print(" Enter the name of the file you want to read or 'exit' to close.\n")


# Logic
while True:
    user_input = input(" Filename or 'exit': ")

    if user_input.lower() == "exit":
        print("\nBye!\n") 
        break
    else:
        read_file_reader(user_input)

input(" \nPress Enter to Finish...")