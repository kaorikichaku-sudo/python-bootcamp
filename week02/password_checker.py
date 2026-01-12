# Imports
from password_checker_utils import (
    check_stenght,
    rules
)

# Program header
print(" PASSWORD STRENGTH-CHECKER\n\n")

# User instructions
print(
    f" Enter passwords, to check their security.\n"
    f" Enter 'rules'  to obtain the requirements for a strong password.\n"
    f" Enter 'exit' to quit.\n\n"

)

# Program logic
while True:
    # User query
    user_input = input(" Password, 'rules' or 'exit': ")

    # Input check and password check
    if user_input.lower() == "exit":
        print("\n")
        break
    elif user_input.lower() == "rules":
        rules()
    else:
        print(check_stenght(user_input))
        

input(" Press Enter to close...")
        
        