from decorators import handle_input_error
from models import Record, AddressBook

phonebook = AddressBook()


@handle_input_error(error_message="Invalid command. Usage: add [ім'я] [номер телефону]")
def add_phone_number(*params) -> str:
    name, phone = params

    contact = phonebook.find(name, raise_error=False)
    if not contact:
        contact = Record(name)
        phonebook.add_record(contact)

    contact.add_phone(phone)

    return "Contact number added."


@handle_input_error(error_message="Invalid command. Usage: change [ім'я] [номер телефону] [новий номер телефону]")
def update_phone_number(*params) -> str:
    name, phone, new_phone = params
    contact = phonebook.find(name)
    contact.edit_phone(phone, new_phone)

    return "Contact number updated."


@handle_input_error(error_message="Invalid command. Usage: delete [ім'я]")
def remove_contact(*params) -> str:
    (name,) = params
    phonebook.delete(name)

    return "Contact deleted."


@handle_input_error(error_message="Invalid command. Usage: contact [ім'я]")
def retrieve_contact(*params) -> Record:
    (name,) = params
    contact = phonebook.find(name)
    return contact


def list_all_contacts() -> list:
    return [str(contact) for contact in phonebook.data.values()]
