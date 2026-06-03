import email
import json
import re
from typing import TypedDict
import logging

logging.basicConfig(
    filename="contacts.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class InvalidContactError(Exception):
    pass


class Contactdata(TypedDict):
    name: str
    phone: str
    email: str


class Contact(TypedDict):
    id: int
    data: Contactdata


contacts: list[Contact] = []


def validate_phone(phone: str) -> bool:
    return phone.isdigit() and len(phone) == 10


def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))


def add_contacts() -> None:
    try:
        name: str = input("Enter name: ")
        if not name:
            raise InvalidContactError("Name cannot be empty")
        phone: str = input("Enter phone: ")
        if not validate_phone(phone):
            raise InvalidContactError("Invalid phone number. Must be 10 digits.")
        email: str = input("Enter email: ")
        if not validate_email(email):
            raise InvalidContactError("Invalid email format.")
        contact: Contact = {
            "id": len(contacts) + 1,
            "data": {"name": name, "phone": phone, "email": email},
        }
        contacts.append(contact)
        logging.info(f"Added contact: {contact}")
        print("contact added sucessfully..............")
    except InvalidContactError as e:
        logging.warning(f"Failed to add contact: {e}")
        print(f"Failed to add contact: {e}")


def view_contacts() -> None:
    if not contacts:
        print("No contacts found")
        return
    for person in contacts:
        print("\n----------------------")
        print("ID:", person["id"])
        print("Name :", person["data"]["name"])
        print("Phone:", person["data"]["phone"])
        print("Email:", person["data"]["email"])


def search_contacts() -> None:
    pattern: str = input("Enter search pattern : ")
    found: bool = False
    for person in contacts:
        name: str = person["data"]["name"]
        email: str = person["data"]["email"]
        if re.search(pattern, name, re.IGNORECASE) or re.search(
            pattern, email, re.IGNORECASE
        ):
            print("\n----------------------")
            print("ID:", person["id"])
            print("Name :", name)
            print("Phone:", person["data"]["phone"])
            print("Email:", email)
            found = True
    if not found:
        logging.info(f"No contacts found matching pattern: {pattern}")
        print("No matching contacts found")
        


def save_contacts():
    try:
        with open("buggysnippet.json", "w") as file:
            json.dump(contacts, file, indent=4)
        logging.info("contacts saved successfully")
        print("Contacts saved successfully")
    except Exception as e:
        logging.error(f"Failed to save contacts: {e}")
        print("Failed to save contacts")

def load_contacts():
    global contacts
    try:
        with open("buggysnippet.json", "r") as file:
            contacts = json.load(file)
        logging.info("contacts loaded successfully")
        print("contact loaded sucessfully...................")
    except FileNotFoundError:
        contacts = []
        logging.error("buggysnippet.json file not found")
        print("no loaded contacts found...........................")


while True:
    print("\n-----------MENU-----------------")
    print('Add contacts Enter :"1"')
    print('view contacts Enter :"2"')
    print('search contacts Enter :"3"')
    print('save contacts Enter :"4"')
    print('load contacts Enter :"5"')
    print('Exit Enter : "6"')
    try:
        choice: int = int(input("Enter your choice: "))
    except ValueError:
        logging.warning("Invalid input for menu choice")
        print("Enter the correct choice.................")
        continue

    if choice == 1:
        add_contacts()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        search_contacts()
    elif choice == 4:
        save_contacts()
    elif choice == 5:
        load_contacts()
    elif choice == 6:
        print("exiting program.......................")
        break
