from contacts_utils import(
    add_contact,
    list_contacts,
    del_contact,
    search_contact
)
print("CONTACTS\n\n")

print(
    f" MENU\n\n"
    f" 1. Add contact\n"
    f" 2. Search contact\n"
    f" 3. List all contacts\n"
    f" 4. Delete contact\n"
    f" 5. Exit\n\n"
)


while True:
    # Query
    query_input = input(" Please Select: ")

    # Exit
    if query_input == "5":
        break

    # List
    elif query_input == "3":
        list_contacts()

    # Delete
    elif query_input == "4":
        del_input = input(" Enter the name to delete: ")
        del_contact(del_input)

    # Search
    elif query_input == "2":
        search_input = input(" Name of searched: ")
        search_contact(search_input)
    # New Contact

    elif query_input== "1":
        name_input = input(" Name for new conract: ")
        number_input = input(f" Number for {name_input}: ")
        add_contact(name_input, number_input)

    else:
        print(" Please select 1 - 5\n\n")
input("\n press...")