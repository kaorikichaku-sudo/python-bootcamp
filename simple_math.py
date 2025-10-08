import os

print("Hi there, this ist the Four-Key on Two-Number Calculator!")
num_one = float(input("Write here your first number: "))
num_two = float(input("Write here the second: "))

Differenz = "wert"
Produkt = "wert"
Quotient = "wert"

if num_one >= num_two:
    Differenz = num_one - num_two
elif num_two > num_one:
    Differenz = num_two - num_one

if num_one >= num_two:
    Quotient = num_one / num_two
elif num_two > num_one:
    Quotient = num_two / num_one

print(f" Erste Zahl: {num_one}\n Zweite Zahl: {num_two}\n\n Summe: {num_one + num_two}\n Differenz: {Differenz}\n Produkt: {num_one * num_two}\n Quotient: {Quotient}\n")

os.system("pause")