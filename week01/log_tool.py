from log_tool_utils import try_create_log, write_log, read_file, delete_logs

# Program-Header
print(" USER-INPUT-LOG\n")


# Create log.txt or open if exists
try_create_log("log.txt")


# Main-menu logic
print("\n Main-menu:\n\n write -> New Log\n show  -> Display all Logs\n clear -> Delete log-file\n exit  -> Close\n\n")

while True:
    user_choice = input("\n Main-menu-Choice: ")

    if user_choice.lower() == "exit":
        print("\n Bye! \n")
        break
    elif user_choice.lower() == "write":
        #Add log logic
        while True:
            user_input = input(" Log or 'back': ")

            # Proof user input
            if user_input.lower() == "back":
                break
            else:
                write_log("log.txt", user_input)
    
    elif user_choice.lower() == "show":
        read_file("log.txt")
    
    elif user_choice.lower() == "clear":
        print(" Are you sure you want to delete all the logs?\n")
        delete_y_n = input(" Y/N: ")
        
        if delete_y_n.lower() == "y":
            delete_logs("log.txt")
        else:
            print("Log not deleted.\n\n")
    
    else:
        print(" Please enter a valid choice.\n\n")


input(" Press Enter to Finish...")




