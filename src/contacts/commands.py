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
        return "Please check your request and specify the contact name, field which you would like to change (phone/email/address/birthday), and the value to change."
    new_value = args[-1]
        # The second-to-last argument is the field (email/address/birthday)
    field_to_change = args[-2].lower()
    # All other arguments are part of the name
    name = ' '.join(args[:-2]).strip()
    # Check "phone" field
    if field_to_change.isdigit():
        field_to_change = args[-3].lower()
        name = ' '.join(args[:-3]).strip() 
  
    # Find the contact by name
    record = book.find(name)
    if record is None:
        return f"Contact not found. Debug: Contact with name '{name}' was not found."

    # Handle the field-to-change
    if field_to_change == "phone":
        if len(args) < 4:
            return "Please provide both the old phone number and the new phone number."
        old_phone = args[-2]  # The old phone number is the third-to-last argument
        print(f"Debug: Trying to change phone from {old_phone} to {new_value}")  # Debugging line
        
        # Ensure the phone validated
        try:
            record.edit_phone(old_phone, new_value)
        except ValueError as e:
            return f"Error changing phone: {str(e)}"
        
        return "Phone changed."
    
    elif field_to_change == "email":
        # Assuming the email is validated using some regex or format check
        if "@" not in new_value or "." not in new_value:
            return "Invalid email format."
        record.email = new_value  # Update the email
        return "Email changed."
    
    elif field_to_change == "address":
        record.address = new_value  # Update the address
        return "Address changed."
    
    elif field_to_change == "birthday":
        try:
            record.add_birthday(new_value)  
        except ValueError:
            return "Invalid birthday format. Please use 'DD.MM.YYYY'."
        return "Birthday changed."
    
    else:
        return "Invalid field. Please choose one of: phone, email, address, birthday."
    


@input_error
def show_phone(args, book):
    # Join all words in args to handle multi-word names
    name = ' '.join(args).strip()
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found")
    return '; '.join(p.value for p in record.phones)

@input_error
def add_birthday(args, book):
    if len(args) < 2:
        raise IndexError("Not enough arguments. Provide a name and a birthday.")
    
    # Join all but the last argument for the name, and treat the last as the birthday
    *name_parts, birthday = args
    name = ' '.join(name_parts).strip()

    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found")
    
    record.add_birthday(birthday)
    return "Birthday added."

@input_error
def show_birthday(args, book):
    name = ' '.join(args).strip()
    print(f"Looking up record for: {name}")
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found")
    return record.birthday or "No birthday set"


@input_error
def birthdays(args, book):
    # Handle the days argument from the command
    if not args:
        return "Please provide the number of days (e.g., 'birthdays 8')."
    
    try:
        days = int(args[0])  # Convert the first argument to an integer
    except ValueError:
        return "Invalid input. Please provide a valid number of days."
    
    # Get upcoming birthdays
    upcoming_birthdays = book.get_upcoming_birthdays(days=days)
    if not upcoming_birthdays:
        return "No upcoming birthdays."
    
    return "\n".join(
        f"{record['name']}: {record['congratulation_date']}"
        for record in upcoming_birthdays
    )

@input_error
def delete_contact(args, book):
    if not args:
        raise ValueError("Please provide the name of the contact to delete.")
    
    name = " ".join(args).strip()
    
    # Find and delete the contact
    record = book.find(name)
    if record is None:
        return f"Contact '{name}' not found."
    
    # Remove the record from the book
    book.delete(name)
    return f"Contact '{name}' has been deleted."