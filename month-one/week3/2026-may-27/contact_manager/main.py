import json
import re
contacts=[]

def add_contacts():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contact = {
    "id": len(contacts) + 1,
    "data": {
        "name":name,
        "phone": phone,
        "email": email
    }
}
    contacts.append(contact)
    print("contact added sucessfully..............")
    
    
    
def view_contacts():
    if not contacts:
        print("No contacts found")
        return
    for  person in contacts:
        print("\n----------------------")
        print("ID:", person["id"])
        print("Name :", person["data"]["name"])
        print("Phone:", person["data"]["phone"])
        print("Email:", person["data"]["email"])
        
def search_contacts():
    pattern = input("Enter search pattern : ")
    found = False
    for person in contacts:
        name = person["data"]["name"]
        email = person["data"]["email"]
        if re.search(pattern, name, re.IGNORECASE) or re.search(pattern, email, re.IGNORECASE):
            print("\n----------------------")
            print("ID:", person["id"])
            print("Name :", name)
            print("Phone:", person["data"]["phone"])
            print("Email:", email)
            found = True
    if not found:
        print("No matching contacts found")   
        
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)
    print("Contacts saved successfully")
    
def load_contacts():
    global contacts
    try:
        with open("contacts.json","r") as file:
            contacts = json.load(file)
        print("contact saved sucessfully...................")
    except FileNotFoundError:
        contacts = []
        print("no saved contacts found...........................")
                
while True:
    print("\n-----------MENU-----------------")
    print(f'Add contacts Enter :"1"')
    print(f'view contacts Enter :"2"')
    print(f'search contacts Enter :"3"')
    print(f'save contacts Enter :"4"')
    print(f'load contacts Enter :"5"')
    print(f'Exit Enter : "6"')
    
    choice = int(input("Enter the choice : "))
    
    
    if choice == 1:
        add_contacts()
    elif choice == 2:
        view_contacts()
    elif choice ==3:
        search_contacts()
    elif choice ==4:
        save_contacts()
    elif choice ==5:
        load_contacts()
    elif choice ==6:
        print("exiting program.......................")
        break
    else:
        print("invalid choice.. Try agin............")
        
        
    