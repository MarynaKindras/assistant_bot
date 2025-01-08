from ..utils.utils import input_error
from .record import Record



@input_error
def add_contact(args, book):
    if len(args) < 2:
        raise ValueError("Please provide both name and phone number.")
    
    # The phone number is the last argument
    phone = args[-1]
    
    # Everything before the last argument is considered the name (can contain spaces)
    name = " ".join(args[:-1])
    
    # Look for an existing record or create a new one
    record = book.find(name)
    message = "Contact updated."
    
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    
    # Add the phone number to the record
    record.add_phone(phone)
    
    # Optional details (address, email, birthday)
    address, email, birthday = None, None, None
    
    # Iterate over remaining arguments and look for specific fields (address, email, birthday)
    for i in range(0, len(args) - 1, 2):  # Iterate in pairs, skipping the last element (phone)
        if i + 1 < len(args):
            if args[i] == 'address':
                address = args[i + 1]
            elif args[i] == 'email':
                email = args[i + 1]
            elif args[i] == 'birthday':
                birthday = args[i + 1]
    
    # Add additional details if found
    if address:
        record.add_address(address)
    if email:
        record.add_email(email)
    if birthday:
        record.add_birthday(birthday)

    # If no address, email, or birthday are added, prompt the user for more details
    if not any([address, email, birthday]):
        response = input("Maybe you want to add more details? Such as address, email, and birthday? (yes/no): ")
        if response.lower() == 'yes':
            additional_info = input("Please enter additional details (e.g., email example@gmail.com birthday DD.MM.YYYY address: text up to 100 symbols): ").split()
            for i in range(0, len(additional_info), 2):
                if i + 1 < len(additional_info):
                    if additional_info[i] == 'address':
                        record.add_address(additional_info[i + 1])
                    elif additional_info[i] == 'email':
                        record.add_email(additional_info[i + 1])
                    elif additional_info[i] == 'birthday':
                        record.add_birthday(additional_info[i + 1])
    
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
