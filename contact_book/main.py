import json
import os
from pathlib import Path
import sys
from contact import * 


def contact_hook(dct):
    if "street" in dct and "plz" in dct:
        return Address(**dct)

    if "first_name" in dct and "last_name" in dct:
        return Contact(**dct)

    return dct

def _creating_file_path(path):
    base_dir = Path(__file__).parent
    return base_dir / path

def _loading_contacts(file_name):
    contact = []
    with open(file_name, "r") as file_data:
        string = file_data.read()
        print(string)
        com_num = json.loads(string, object_hook=contact_hook)
        contact.extend(com_num)
        file_data.close()
    return contact

def _create_contact():
    first_name = input("Vorname ")
    last_name = input("Nachname ")
    contact = Contact(first_name=first_name,last_name=last_name)
    return contact

def _print_contacts(contacts):
    for contact in contacts:
        print(contact.first_name +" "+ contact.last_name)
    
def _write_to_file(file_name, contacts):

    # komplette Liste zurückschreiben
    with open(file_name, "w") as file:
        json.dump(contacts, file, indent=4, cls=EncodeContact)


#Mini-Kontaktbuch – Kontakte speichern, suchen, bearbeiten, als JSON abspeichern/laden. 
#Ziel: Dataclasses, JSON-Serialisierung, pathlib, Exception Handling mit eigenen Exceptions.
if __name__== "__main__":
    print("Python JSON contact book")
    file_name = "contacts.json"
    file_path = _creating_file_path(file_name)
    contacts=[]
    if(Path.exists(file_path) is True):
        contacts = _loading_contacts(file_path)
    else:
        open(_creating_file_path(file_path), "x")
    
    if len(sys.argv) == 1:
        print("Please provide a command. Possible Commands:")
        print("print_con: listing all current contacts")
        print("create_con : creating a new contact")
        print("print_single_contact : Auflistung von contact details unter Angbe von Vor- und Nachname")
        print("change_single_contact : Bearbeiten von contact details unter Angbe von Vor- und Nachname")
        print("delete_single_contact : Löschen von contact unter Angabe von Vor- und Nachname")
    
    if len(sys.argv) == 2:
        match sys.argv[1]:
            case "create_con":
                print("Create a new contact")
                contact = _create_contact()
                contacts.append(contact)
                _write_to_file(file_path, contacts)
            case ("print_con"):
                print("All contacts")
                _print_contacts(contacts)
            case ("print_single_contact"):
                print("Single Contact")
            case ("change_single_contact"):
                print("Change single contact")
            case ("delete_single_contact"):
                print("Delet single contact")

