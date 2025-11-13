from notes_utils import create_file, open_file, read_file
import os

print("NOTES MANAGER\n\n")



# Welcome user
print(" With this program you can create, add and read notes!\n")

# User instructions
print(f"\n  Enter:\n 'Create' for a new file.\n 'Note' for new note.\n 'Read' to see notes.\n 'Exit' to close.\n")
    
# Program logic
while True:
    # User input
    choice = input("\n Choice: ")

    # Proof choice
    if choice.lower() == "exit":
        print(" Bye!")
        break
    
    elif choice.lower() == "create":
        file_name_create = input(" Name for new file: ")
        create_file(file_name_create)
        continue
    
    elif choice.lower() == "note":
        file_to_open = input(" Name of file: ")
        if not os.path.exists(file_to_open):
            print(" File does not exist!")
            continue
        print("\n Write your new note or 'back' to get to the main-menu.")
        while True:
            note_choice = input("\n Note or 'back': ")
            if note_choice.lower() == "back":
                break
            else:
                open_file(file_to_open, note_choice)
                continue

    elif choice.lower() == "read":
        print("\n Enter name of file or 'back' to get to the main-menu.")
        while True:
            file_to_read = input("\n Name of file you want to read or 'back': ")
            if file_to_read.lower() == "back":
                break
            else:
                read_file(file_to_read)
                continue 
    
    else:
        print(" Please enter a valid option.")
        continue
    

input("\n Press Enter to Finish...")
