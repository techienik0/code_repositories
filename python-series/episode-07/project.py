# Episode 7: Project - Simple Contact Book
# Using lists and dictionaries to build something useful!

def add_contact(contacts, name, phone, email):
    """Add a new contact to the contact book"""
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print(f"Contact {name} added successfully!")

def view_contacts(contacts):
    """Display all contacts"""
    if not contacts:
        print("No contacts found!")
        return
    
    print("\n=== CONTACT BOOK ===")
    for i, contact in enumerate(contacts, 1):
        print(f"\n{i}. {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")

def search_contact(contacts, name):
    """Search for a contact by name"""
    found = []
    for contact in contacts:
        if name.lower() in contact["name"].lower():
            found.append(contact)
    
    if found:
        print(f"\nFound {len(found)} contact(s):")
        for contact in found:
            print(f"  {contact['name']} - {contact['phone']} - {contact['email']}")
    else:
        print(f"No contact found with name '{name}'")

def delete_contact(contacts, name):
    """Delete a contact by name"""
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            removed = contacts.pop(i)
            print(f"Contact {removed['name']} deleted!")
            return True
    print(f"Contact '{name}' not found!")
    return False

def contact_book():
    """Main contact book program"""
    contacts = []  # List to store all contacts (each contact is a dictionary)
    
    print("=== SIMPLE CONTACT BOOK ===")
    print("Manage your contacts easily!")
    
    while True:
        print("\nOptions:")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(contacts, name, phone, email)
        
        elif choice == "2":
            view_contacts(contacts)
        
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(contacts, name)
        
        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_contact(contacts, name)
        
        elif choice == "5":
            print("Goodbye! Your contacts are saved in memory.")
            break
        
        else:
            print("Invalid choice! Try again.")

# Run the contact book
if __name__ == "__main__":
    contact_book()
