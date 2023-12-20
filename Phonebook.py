phone_book = {}

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    phone_book[name] = phone_number
    print("Contact added successfully!")

def search_contact():
    name = input("Enter contact name: ")
    if name in phone_book:
        print(f"Phone number of {name}: {phone_book[name]}")
    else:
        print(f"{name} not found in phone book")

def view_all_contacts():
    if len(phone_book) == 0:
        print("Phone book is empty!")
    else:
        print("Phone book:")
        for name, phone_number in phone_book.items():
            print(f"{name}: {phone_number}")

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. View all contacts")
    print("4. Exit")

    choice = int(input("\nEnter your choice (1-4): "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        view_all_contacts()
    elif choice == 4:
        break
    else:
        print("Invalid choice!")
