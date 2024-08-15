# CONTACT MANAGEMENT SYSTEM

contacts = {}

def add_contact():
    
    "ADD THE NAME / PHONE NUMBER / EMAIL / ADDRESS / CONTACT NAMES"
    name = input("enter name: ")
    phone = input("enter phone number: ")
    email = input("enter email: ")
    address = input("enter address: ")
    contacts [name] = {'phone': phone, 'email': email, 'address': address}
    print("The Contact Added Successfully!")

# VIEWING OF THE CONTACTS
def view_contacts():
    if not contacts:
        print("No contacts were available!")
    else:
        for name , details in contacts.items():
            print(f"Name: {name}, phone: {details['phone']}") 

# SEARCHING OF THE CONTACTS
def search_contacts():
    query = input("enter the name or phone number to search: ")
    for name , details in contacts.items():
        if query in name or query in details ['phone']:
            print(f"name: {name}, phone: {details['phone']}, email: {details['email']}, address: {details['address']}") 
            return
    print("contact not found!") 

# UPDATING OF THE CONTACTS
def update_contacts():
    name = input("enter the name of the contact to update: ")
    if name in contacts:
        phone = input("enter the new phone number (optional): ")
        email = input("enter the new email (optional): ")
        address = input("enter the new address (optional): ")
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email 
        if address:
            contacts[name]['address'] = address
        print("The contacts were updated successfully!")
    else:
        print("contacts were not found!")

# DELETING THE CONTACTS 
def delete_contacts():
    name = input("enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("The contact deleted successfully!")
    else:
        print("The contact were not found! ")

while True:
    print("\nContact Management System")
    print("1. Add contact")
    print("2. View contact") 
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")   

    choice = input("enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contacts()
    elif choice == '4':
        update_contacts()
    elif choice == '5':
        delete_contacts()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again. ")                            