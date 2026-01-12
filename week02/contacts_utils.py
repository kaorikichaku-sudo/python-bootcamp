# Functions

def add_contact(contact, number):
    contact = contact.strip()
    number = str(number).strip()

    with open("contacts.txt", "a") as f:
        f.write(f"{contact} | {number}\n")
    print("\n Contact added successfully.\n\n")
    
# ---------------------------------------------------------------------------    
def list_contacts():
    try:
        with open("contacts.txt", "r") as f:
            content = f.readlines()
            print("\n --- Contacts ---\n")

            if not content:
                print(" This file is empty.\n")
                print(" --------------- \n\n")
            else:
                for line in content:
                    print(line)
                print(" --------------- \n\n")
    except FileNotFoundError:
        print(" No file found.\n\n")

# ---------------------------------------------------------------------------    
def search_contact(user_input):
    user_input = user_input.strip()
    found = False

    try:
        with open("contacts.txt", "r") as f:
            content = f.readlines()

            for line in content:
                stripped = line.strip()
                if not stripped:
                    continue

                splitted = stripped.split(" | ", 1)
                parts = splitted[0]

                if user_input == parts:
                    print(f"\n {line}\n\n")
                    found = True
            if not found:
                    print(f"\n Contact {user_input} not found.\n\n")
    except FileNotFoundError:
        print(" No file found.\n\n")

# ---------------------------------------------------------------------------   
def del_contact(user_input):
    user_input = user_input.strip()

    try:
        with open("contacts.txt", "r") as f:
            content = f.readlines()
            new_lines = []
            deleted = False
            for line in content:
                stripped = line.strip()
                if not stripped:
                    continue

                splitted_line = stripped.split(" | ", 1)
                parts = splitted_line[0]
                if parts == user_input:
                    deleted = True
                else:
                    new_lines.append(line)
            if deleted == True:
                print("\n Contact successfully deleted.\n\n")
            with open("contacts.txt", "w") as f:
                f.writelines(new_lines)

    except FileNotFoundError:
        print(" No file found.\n\n")