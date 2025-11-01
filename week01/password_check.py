right_password = "PythonRocks"
count = 0
max_tries = 3

print(" Hi there!\n to enter, please write the password.\n")

while True:
    user_input = input(" Password: ")

    if user_input == right_password:
        print(" Login succcessfully.\n")
        break
    else:
        count += 1
        tries_left = max_tries - count

        if tries_left > 0:
            print(f" That's not right, you have: {tries_left} left.\n")
        else:
            print(f" That's not right, tries left: {tries_left} access denied.\n")
            break


input("Press Enter to finish...")