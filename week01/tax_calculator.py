print("TAX CALCULATOR\n\n") 

# Define functions
def cal_tax(price, tax_rate=0.19):
    return price * (1 + tax_rate)

def is_number(value):
    try:
        float(value)
        return  True
    except ValueError:
        return False


# User instructions
print(" Please enter below a net price to get the gross price calculated (19%). To finish enter 'exit'\n")


# Input query
while True:
    user_price = input(" Enter the price here: ") 

    
    # Proof input
    if user_price.lower() == "exit":
        print(" \nBye!\n")
        break
    elif user_price.strip() == "":
        print(" Error, please enter something!\n")
        continue
    

    # Prepare input
    user_price = user_price.replace(",", ".").strip()


    # Test on numbers
    if not is_number(user_price):
        print(" Error, that was not a number.\n")
        continue


    # Conversion
    user_price = float(user_price.strip())
    

    # Calculat
    print(f"\n Net price: {user_price:.2f}\n Gross price: {cal_tax(user_price):.2f}\n")


input("Press Enter to exit.")