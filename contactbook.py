class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {
            'Phone Number': phone_number,
            'Email': email,
            'Address': address
        }

    def view_contacts(self):
        for name, contact_info in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone Number: {contact_info['Phone Number']}")
            print(f"Email: {contact_info['Email']}")
            print(f"Address: {contact_info['Address']}")
            print("-" * 20)

    def search_contact(self, keyword):
        results = []
        for name, contact_info in self.contacts.items():
            if keyword in name or keyword in contact_info['Phone Number']:
                results.append((name, contact_info))
        return results

    def update_contact(self, name, phone_number, email, address):
        if name in self.contacts:
            self.contacts[name] = {
                'Phone Number': phone_number,
                'Email': email,
                'Address': address
            }
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")


# User Interface
contact_book = ContactBook()

while True:
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact_book.add_contact(name, phone_number, email, address)

    elif choice == '2':
        contact_book.view_contacts()

    elif choice == '3':
        keyword = input("Enter name or phone number to search: ")
        search_results = contact_book.search_contact(keyword)
        if search_results:
            for name, contact_info in search_results:
                print(f"Name: {name}")
                print(f"Phone Number: {contact_info['Phone Number']}")
                print(f"Email: {contact_info['Email']}")
                print(f"Address: {contact_info['Address']}")
                print("-" * 20)
        else:
            print("No matching contacts found.")

    elif choice == '4':
        name = input("Enter name of the contact to update: ")
        phone_number = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contact_book.update_contact(name, phone_number, email, address)

    elif choice == '5':
        name = input("Enter name of the contact to delete: ")
        contact_book.delete_contact(name)

    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
