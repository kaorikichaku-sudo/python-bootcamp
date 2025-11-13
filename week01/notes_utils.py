# Utils for write_notes

# Define functions
def create_file(file_name):
    try:
        with open(file_name, "x") as f:
            print(f" {file_name} created successfully.")
    except FileExistsError:
        print(f" File: {file_name} already exists. No new file created.")


def open_file(file_name, note):
    with open(file_name, "a") as f:
        f.write(note + "\n\n")
    print(" Note successfully added.")


def read_file(file_name):
    try:
        with open(file_name, "r") as f:
            content = f.readlines()
        print("\n --- Contents of file ---\n")
        if not content:
            print(" This file is empty.")
        else:
            for line in content:
                print(line.strip())
        print("\n ------------------------\n")
    except FileNotFoundError:
        print(" This File does not exists. Please try again.\n")


def read_file_reader(file_name):
    try:
        with open(file_name, "r") as f:
            content = f.readlines()
        if not content:
            print("\n This file is empty.\n")
        else:
            c = 0
            print("\n")
            for line in content:
                c += 1 
                print(f" {c}: {line.strip()}\n")
            print(f"\n Total: {c}\n\n")
    except FileNotFoundError:
        print(" This File does not exists. Please try again.\n")