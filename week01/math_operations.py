# Define functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return None      
    else:
        return a / b
    

# Welcome user
print("Hello User, enter two numbers and you will get the Addition, Subtraction, Multiplication and Division from them. Or enter 'endnow' to finish.\n")


while True:
    # Number query
    zahlen = []
    zahlen.append(input(" First number or endnow: "))
    zahlen.append(input(" Second number or endnow: "))


    # Proof input
    if zahlen[0].lower() == "endnow" or zahlen[1].lower() == "endnow":
        print(" \nBye!\n")
        break
    elif zahlen[0].strip() == "":
        print(" Error first number, please enter something!\n") 
        continue 
    elif zahlen[1].strip() == "": 
        print(" Error second number, please enter something!\n.")   
        continue

    for index in range(len(zahlen)):
        zahlen[index] = float(zahlen[index].replace(",", ".").strip())
            
    # Print result
    print(f" Zahl 1: {zahlen[0]}\n Zahl 2: {zahlen[1]}\n Summe: {add(*zahlen)}\n Differenz: {sub(*zahlen)}\n Produkt: {mul(*zahlen)}\n Quotient: {div(*zahlen)}\n")

        
input("Press Enter to Finisch...")  
