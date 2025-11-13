# Define function
def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero!")
        return None
    except TypeError:
        print("Erro: invalid digit.")
        return None

def try_convert(value):
    try:
        return float(value)
    except ValueError:
        print(" This is not a valid number, please try again.")
        return None
    

# User instruction
print(" Enter below 2 numbers to divide or write 'exit' to close.\n\n")

# Logic
while True:

    first_number = input(" First number or 'exit': ")
    if first_number.lower() == "exit":
        break
    else:
        second_number = input(" Second number or 'exit': ")
    if second_number.lower() == "exit":
        print("\n Bye!\n")
        break
    else:
        # Prepare input
        first_number = first_number.replace(",", ".").strip()
        second_number = second_number.replace(",", ".").strip()
        
        first_number = try_convert(first_number)
        second_number = try_convert(second_number)

        if first_number is None or second_number is None:
            continue

        # Calculate
        print(f"\n Result: {safe_division(first_number, second_number):.2f}\n\n")

