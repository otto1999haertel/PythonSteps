import json
from pathlib import Path
from contact import * 
import jsonpickle


def _creating_file_path(path):
    base_dir = Path(__file__).parent
    return base_dir / path

def _loading_contacts(path):
    return []




#Mini-Kontaktbuch – Kontakte speichern, suchen, bearbeiten, als JSON abspeichern/laden. 
#Ziel: Dataclasses, JSON-Serialisierung, pathlib, Exception Handling mit eigenen Exceptions.
if __name__=="__main__":
    print("Python JSON contact book")
    file_path = _creating_file_path("contacts.json")
    contacts=[]
    if(Path.exists(file_path) is True):
        contacts = _loading_contacts(file_path)
    c1 = Contact("Otto", "Haertel")
    c1.company="Siemens"
    a1 = Address("Kirchstrasse", 16, "Grossgrabe", "02994")
    c1.address = a1

    empJSON = jsonpickle.encode(c1, unpicklable=False)
    print(empJSON)
    
