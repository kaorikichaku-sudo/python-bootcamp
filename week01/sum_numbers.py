print(f" Hello, this is the addition calculator. Enter as many numbers as you like. To finish, type 'stop'.\n")

user_numbers = 0

while True:

    user_input = input(" Number or 'stop': ")

    if user_input == "stop":
        break
    elif not user_input.isdigit():
        print(" That's not a number mate -.- try it again.")
    else:
        user_numbers = user_numbers + int(user_input)

print(f"\n result: {user_numbers}\n")
input("Press Enter to finish...")