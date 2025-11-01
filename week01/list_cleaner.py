print(" List Cleaner\n\n")

list_content = [13, 89, 143, 596, 62]
print_list = []
print(f" List: {list_content}\n")


for num in list_content:
    if num < 100:
        print_list.append(num)
    else:
        continue

print(f" Clean list: {print_list}")
print("\n\n")

input(" Press Enter to finisch...")