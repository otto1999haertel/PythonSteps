from dataclasses import dataclass
import datetime
import json
from json import JSONEncoder

@dataclass
class Contact():
    first_name:str
    last_name : str
    birthday:datetime
    company: str
    email : str
    address : Address

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


@dataclass
class Address():
    street:str
    house_number : str
    place:str
    plz:str

class EncodeContact(JSONEncoder):
    def default(self, o):
        return o.__dict__