from components.tools import input_error
from components.records import Record

@input_error
def add_contact(args, contacts):
    name, phone, *_ = args

    if name in contacts:
        user = input("Do you want to overwrite the contact? (yes/no): ").strip().lower()

        if user == "yes":
            contacts.add_record(Record(name))
            contacts[name].add_phone(phone)
            return "Contact updated"
        elif user == "no":
            return "Contact not added"
        else:
            return "Invalid command."
    else: 
        contact = Record(name)
        contact.add_phone(phone)
        contacts.add_record(contact)
        return "Contact added."

# @input_error 
# def show_all(contacts):
#     return "\n".join([str(contact) for contact in contacts.data.values()])

@input_error   
def change_number(args, contacts):
    name, old_phone, new_phone = args
    record = contacts.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Phone number changed"
    else:
        return f"{name} not found"

@input_error
def print_phone(args, contacts):
    name, *ar = args
    record = contacts.find(name)
    if record:
        return '; '.join(phone.value for phone in record.phones)
    else:
        return f"{name} not found"

@input_error
def add_birthday(args, contacts):
    name, date = args
    record = contacts.find(name)
    if record:
        record.add_birthday(date)
        return f"Birthday added for {name}."
    else:
        return f"{name} not found."

@input_error
def show_birthday(args, contacts):
    name, *ar = args
    record = contacts.find(name)
    if record:
        return str(record.birthday.value) if record.birthday else "Birthday not set."
    else:
        return f"{name} not found."

@input_error
def birthdays(args, contacts):
    upcoming_birthdays = contacts.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No upcoming birthdays in the next week."
    return "\n".join(f"{contact['name']}: {contact['birthday']}" for contact in upcoming_birthdays)
