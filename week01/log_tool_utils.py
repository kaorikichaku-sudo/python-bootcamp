from datetime import datetime


# Define functions
def current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def try_create_log(filename):
    try:
        with open(filename, "x") as f:
            f.write(f"{current_timestamp()} log.txt -> created at programstart.\n\n")
        print(" log.txt created.\n")
    except FileExistsError:
        pass


def write_log(file_name, log):
    with open(file_name, "a") as f:
        f.write(f"{current_timestamp()} {log}\n\n")
    print(" Log captured successfully.\n")


def read_file(file_name):
    try:
        with open(file_name, "r") as f:
            content = f.readlines()
        print("\n\n --- Contents of file ---\n")
        if not content:
            print(" This file is empty.")
        else:
            for line in content:
                print(line.strip())
        print("\n ------------------------\n")
    except FileNotFoundError:
        print(" This File does not exist. Please try again.\n")


def delete_logs(filename):
    with open(filename, "w") as f:
        f.write("")
    print(" Logs successfully deleted.\n\n")
