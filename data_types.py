
import os

# Anlegen der Variablen 
name = "Maria"
alter = 13
groeße = 1.55


# Ausgabe

output = f"{name}, {type(name)}\n\n{alter}, {type(alter)}\n\n{groeße}, {type(groeße)}\n\n"
print(output)

#oder

print(f"{name}, {type(name)}\n")
print(f"{alter}, {type(alter)}\n")
print(f"{groeße}, {type(groeße)}\n")

# Ender der Ausgabe

#Damit die shell nicht shcließt
os.system("pause")
