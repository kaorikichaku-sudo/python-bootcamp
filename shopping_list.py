print("Smart Shopping List")
print("Enter items for your shopping list, type 'done' to finish.\n")

shopping_list = []

while True:
    user_input = input("Item (or 'done'): ").strip()
    if not user_input:  # ignore empty inputs
        continue
    if user_input.lower() == "done":
        break
    shopping_list.append(user_input)

print("\nYour shopping list:\n")
for item in shopping_list:
    print(f" - {item}")

input("\n\nPress Enter to finish...")