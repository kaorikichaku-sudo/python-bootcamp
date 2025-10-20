# Greeting and base
print(f" Hello! This program will list every number from 0 up to the number you enter and tell you if it's even or odd.\n")

user_input = 0

# User input and logic
while True:
    number_text = input(" Your number: ")

    if "." in number_text or "," in number_text:
        print(f" That's not a whole number, please try it again.^\n")
    elif not number_text.isdigit():
        print(f" That's not a number, please try it again.\n")
    else:
        user_input = int(number_text)
        break

# Convert to an iterable object and output
print_input = range(1, user_input + 1)

for number in print_input:
    if number % 2 == 0:
        print(f" {number}: even")
    else:
        print(f" {number}: odd")

    
input("\nPress Enter to finish...")