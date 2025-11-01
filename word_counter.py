print(" Word Counter")
print(" Enter a sentence Below and this aplication will coutn and display the words of your sentence. To finish enter EndNow\n\n")

while True:
    user_input = input(" sentence: ").strip()
    if user_input.lower() == "endnow":
        print("\n")
        break
    words = user_input.split()
    print(f"\n Text: {user_input}")
    print(f" count: {len(words)}\n\n")
        

