print(" Vowel Counter")
print(" Enter below a word or sentence and this application will count and display the vowels in your input. Enter EndNow to finish.\n\n")


while True:
    user_input = input(" Enter here your word or sentence: ")
    

    
    if user_input == "EndNow":
        break
    else:
        count = 0
        print(f"\n Text: {user_input}")
        for char in user_input.lower():
            if char in "aeiou":
                count += 1
        print(f" vowel count: {count}\n\n")