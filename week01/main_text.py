from text_utils import word_count, vowel_count

# Welcome user
print(" WORD & VOWEL COUNTER\n\n")
print(" Enter your sentence bellow and you will get the word and vowel count.\n")

# Program
while True:
    user_input = input(" Enter your sentence or 'exit' here: ")

    
    # Logic
    if user_input.lower() == "exit":
        print("\nBye!\n")
        break
    else:
        print(f" \n\n Word count: {word_count(user_input)}\n Vowel_count: {vowel_count(user_input)}\n\n")
        continue

# End of program
input("\nPress Enter to Finish...")