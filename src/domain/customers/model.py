from typing import List

class Customers:
    def __init__(self, first_name, last_name, phone_number, genre, document_id, birth_date) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.genre = genre
        self.document_id = document_id
        self.birth_date = birth_date
        self.addresses = []

    def add_address(self, new_address):
        if new_address.primary == False:
            self.addresses.append(new_address)
        main = [address for address in self.addresses if address.primary == True]
        if main:
            for address in main:
                address.primary = False
        self.addresses.append(new_address)