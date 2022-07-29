from email import utils
from base_repo import BaseRepository
from address_utils import AddressUtils
import json
import re

class AddressRepo(BaseRepository):

    utils = AddressUtils()
    address_book = None

    def __init__(self) -> None:
        super().__init__("address-book.json")

    def get_address(self):
        if self.address_book == None:
            self.address_book = json.loads(super().readFile())
        return self.address_book

    def add_new_address(self, address_entry):
        address_entry["id"] = self.utils.generateId()
        self.get_address()["address-book"].append(address_entry)
        self.save()

    def find_address_book(self, name, address):
        name = name.lower().strip()
        address = address.lower()

        stringCompare = lambda a,b: (a.lower() == b or b =="" or re.findall(b,a))

        result = filter(lambda entry:stringCompare(entry.get("name",""),name) 
                and stringCompare(entry.get("address",""),address),
                self.get_address()["address-book"])
            
        return list(result)

    def update_address(self, address_entry):
        result = list(filter(lambda entry: entry.get("id") == address_entry.get("id"), 
                    self.get_address()["address-book"]))
        result[0] = address_entry
        self.save()

    def save(self):
        super().writeFile(json.dumps(self.address_book, indent=2))

    def delete_address(self, address_entry):
        index = 0
        for entry in self.get_address()["address-book"]:
            if entry.get("id") == address_entry.get("id"):
                break
            index = index + 1
        self.get_address()["address-book"].pop(index)
        self.save()