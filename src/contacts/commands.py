from ..utils.utils import input_error
from .record import Record


@input_error
def add_contact(args, book):
    if len(args) < 2:
        raise IndexError
    
    name, phone = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book):
        if len(args) < 3:
            raise IndexError
        name, old_phone, new_phone = args
        record = book.find(name)
        if record is None:
            raise KeyError
        record.edit_phone(old_phone, new_phone)
        return "Phone changed."

@input_error
def show_phone(args, book):
        name = args[0]
        record = book.find(name)
        if record is None:
            raise KeyError
        return '; '.join(p.value for p in record.phones)

@input_error
def add_birthday(args, book):
    if len(args) < 2:
        raise IndexError
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.add_birthday(birthday)
    return "Birthday added."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    return record.birthday

@input_error
def birthdays(args, book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No upcoming birthdays."
    return "\n".join(
        f"{record['name']}: {record['congratulation_date']}"
        for record in upcoming_birthdays
    )
