# Contact Book
contact_book = {}  # Dictionary to store names and phone numbers

def add_contact():
    name = input("Enter the contact's name: ").strip()
    number = input(f"Enter {name}'s phone number: ").strip()
    
    # Store in dictionary
    contact_book[name] = number
    print(f"{name} has been added with number {number}!")

def view_contacts():
    if contact_book:
        print("\nHere are your contacts:")
        for name, number in contact_book.items():
            print(f"- {name}: {number}")
    else:
        print("\nYour contact book is empty :(")

def search_contact():
    name = input("Enter the name you want to search for: ").strip()
    if name in contact_book:
        print(f"{name}'s number is {contact_book[name]}")
    else:
        print(f"{name} is not in your contacts!")

def delete_contact():
    name = input("Please enter who you would like to remove!")
    if name in contact_book:
        remove_contact(name)
    else:
        print("That name is not in your contact book!")

def remove_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} has been removed.")

print("Welcome to your contact book!")
while True:
    initial = input("\nWhat would you like to do today? (Add, View, Search, Remove, Exit): ").strip().lower()
    
    if initial.lower() == "add":
        add_contact()
    elif initial.lower() == "view":
        view_contacts()
    elif initial.lower() == "search":
        search_contact()
    elif initial.lower() == "exit":
        print("Goodbye!")
        break
    elif initial.lower() == "remove":
        delete_contact()
    else:
        print("Invalid option. Please choose from: Add, View, Search, or Exit.")

