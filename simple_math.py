print("Hi there, this ist the Four-Key on Two-Number Calculator!")
num_one = float(input("Write here your first number: "))
num_two = float(input("Write here the second: "))

differenz = None
produkt = None
quotient = None

if num_one >= num_two:
    differenz = num_one - num_two
elif num_two > num_one:
    differenz = num_two - num_one

if num_two == 0 or num_one == 0:
    quotient = "undefined (division by zero)"
elif num_one >= num_two:
    quotient = num_one / num_two
else: 
    quotient = num_two / num_one

print(f" Erste Zahl: {num_one}\n Zweite Zahl: {num_two}\n\n Summe: {num_one + num_two}\n differenz: {differenz}\n produkt: {num_one * num_two}\n quotient: {quotient}\n")

input("Press Enter to finish...")