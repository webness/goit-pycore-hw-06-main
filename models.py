import re

from collections import UserDict

class Field:
    def __init__(self, value: any) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Field):
            return False

        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

class Name(Field):
    def __init__(self, name: str) -> None:
        super().__init__(name)


class Phone(Field):
    pattern = r"[+\d]"
    country_code = "38"

    def __init__(self, raw_phone: str) -> None:

        phone = "".join(re.findall(self.pattern, raw_phone))

        if not phone.startswith("+"):
            phone = re.sub(fr"^({self.country_code})?", f"+{self.country_code}", phone)

        if len(phone) != 13:
            raise PhoneFormatError("Invalid phone number.")

        super().__init__(phone)

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        if self.find_phone(phone):
            raise ContactError("Phone number already exists.")

        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        existing_phone = self.find_phone(phone)
        if existing_phone:
            self.phones.remove(existing_phone)

    def edit_phone(self, phone: str, new_phone: str):
        existing_phone = self.find_phone(phone)
        if not existing_phone:
            raise ContactError("No such phone number.")

        if self.find_phone(new_phone):
            raise ContactError("New phone number already exists.")

        self.phones[self.phones.index(existing_phone)] = Phone(new_phone)

    def find_phone(self, phone: str) -> Phone | None:
        target_phone = Phone(phone)
        return next((p for p in self.phones if p == target_phone), None)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        if record.name in self.data:
            raise ContactError("Contact already exists.")

        self.data[record.name] = record

    def find(self, name: str, raise_error: bool = True) -> Record | None:
        name = Name(name)

        if name not in self.data:
            if raise_error:
                raise ContactError("No such contact.")
            return None

        return self.data[name]

    def delete(self, name: str):
        name = Name(name)

        if name in self.data:
            del self.data[name]

class ContactError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class PhoneFormatError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
