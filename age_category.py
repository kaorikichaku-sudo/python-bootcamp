print(f" Hello mate!\n to start, write your age.\n")

while True:
    age_text = input(" your age: ")
    
    # Prove for decimals (dot or komma)
    if "." in age_text or "," in age_text:
        print("Tat's a decimal number, mate...")
        continue
    elif  not age_text.isdigit():
        print("Tat's not an age -.- (please enter a whole number.)")
        continue
    else:
        user_age = int(age_text)
        break   # input is aprooved, end loop


# Age-category
if user_age <= 13:
    print(" That means you're part of the child-category.")
elif user_age in range(14, 18):
    print(" That means you're part of the Teenager-category.")
elif user_age in range(18, 65):
    print(" That means you're part of the Adult-category.")
elif user_age in range(65,101):
    print(" That means you're part of the Senior-category.")
else:
    print(" Wow, That means you're part of the Minority_category.")

input("\nPress any button to finish...")