"""
This module contains functions for managing and interacting with contacts in an address book.

The following operations are provided:
1. `add_contact` - Adds a new contact to the address book with a name, phone number, and optional details such as address, email, and birthday.
2. `change_contact` - Modifies an existing contact by changing specified fields such as phone number, email, address, or birthday.
3. `show_contact` - Retrieves and displays contact details by searching for a contact based on name or email.
4. `add_birthday` - Adds or updates a contact's birthday.
5. `show_birthday` - Displays a contact's birthday.
6. `birthdays` - Displays a list of upcoming birthdays within a specified number of days.
7. `delete_contact` - Deletes a contact from the address book after confirming the deletion.
Each function includes appropriate validation and error handling to ensure proper contact management. The input_error decorator is used to catch common input-related errors such as invalid arguments or missing information.
"""
from src.utils.utils import input_error
from src.contacts.fields import  Phone
from .record import Record


def add_contact(args, book):
    """
    Function to handle adding a contact.
    """
    # Check if there are enough arguments (at least a name and phone number)
    if len(args) < 2:
        return "Error: Invalid command. Try again with correct data."

    # The phone number is the last argument
    phone = args[-1]

    # Extract the name from the arguments
    name_end_index = args.index('address') if 'address' in args else len(args) - 1
    name = " ".join(args[:name_end_index]).strip()

    # Look for an existing record or create a new one
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    # Add the phone number to the record
    try:
        phone = Phone(phone)  # Assuming Phone validation here
        record.add_phone(phone.value)
    except ValueError as e:
        return str(e)  # Return the error if phone validation fails

    # Extract additional details (address, email, birthday)
    address, email, birthday = None, None, None
    i = 0

    while i < len(args):
        if args[i] == 'address':
            address_words = []
            i += 1
            while i < len(args) and args[i] not in ['email', 'birthday', 'phone']:
                address_words.append(args[i])
                i += 1
            address = " ".join(address_words).strip()

        elif args[i] == 'email':
            if i + 1 < len(args):
                email = args[i + 1].strip()
            i += 2

        elif args[i] == 'birthday':
            if i + 1 < len(args):
                birthday = args[i + 1].strip()
            i += 2

        else:
            i += 1

    # Add the extracted details to the record
    if address:
        record.add_address(address)
    if email:
        record.add_email(email)
    if birthday:
        record.add_birthday(birthday)

    # Prompt the user for additional details if none were provided
    if not any([address, email, birthday]):
        response = input("Maybe you want to add more details? Such as address, email, and birthday? (yes/no): ")
        if response.lower() == 'yes':
            additional_info = input("Please enter additional details (e.g., email example@gmail.com birthday DD.MM.YYYY address: text up to 100 symbols): ").split()

            # Process the additional info
            i = 0
            while i < len(additional_info):
                if additional_info[i] == 'address':
                    address_words = []
                    i += 1
                    while i < len(additional_info) and additional_info[i] not in ['email', 'birthday']:
                        address_words.append(additional_info[i])
                        i += 1
                    address = " ".join(address_words).strip()
                elif additional_info[i] == 'email':
                    if i + 1 < len(additional_info):
                        email = additional_info[i + 1].strip()
                    i += 2
                elif additional_info[i] == 'birthday':
                    if i + 1 < len(additional_info):
                        birthday = additional_info[i + 1].strip()
                    i += 2
                else:
                    print("Invalid command in the additional details. The contact has been added without additional information.")
                    return message  # If the additional input is invalid, return the original message

            # Add the parsed details to the record
            if address:
                record.add_address(address)
            if email:
                record.add_email(email)
            if birthday:
                record.add_birthday(birthday)

    return message

    
@input_error
def change_contact(args, book):
    """
    function to handle changes in the contact
    """
    if len(args) < 3:
        return "Please check your request and specify the contact name, field to change (phone/email/address/birthday), and the new value."

    # Identify the field to change and its new value
    field_to_change = None
    new_value_start = None

    # Find the keyword for the field to change and extract the new value
    for i in range(len(args)):
        if args[i].lower() in ['phone', 'email', 'address', 'birthday']:
            field_to_change = args[i].lower()
            new_value_start = i + 1
            break

    if not field_to_change or new_value_start is None:
        return "Please specify a valid field to change (phone/email/address/birthday)."

    # Extract the name and new value
    name = " ".join(args[:i]).strip()
    new_value = " ".join(args[new_value_start:]).strip()

    # Validate the input
    if not name:
        return "Contact name is required."
    if not new_value:
        return f"New value for {field_to_change} is required."

    # Find the contact by name
    record = book.find(name)
    if record is None:
        return f"Contact not found. Debug: Contact with name '{name}' was not found."

    # Handle the field-to-change logic
    if field_to_change == "phone":
        if len(args[new_value_start:]) < 2:
            return "Please provide both the old phone number and the new phone number."
        old_phone = args[new_value_start].strip()  # First part of new_value is the old phone
        new_phone = " ".join(args[new_value_start + 1:]).strip()  # Remaining parts are the new phone

        print(f"Debug: Trying to change phone from {old_phone} to {new_phone}")  # Debugging line
        try:
            record.edit_phone(old_phone, new_phone)
        except ValueError as e:
            return f"Error changing phone: {str(e)}"
        return "Phone changed."

    elif field_to_change == "email":
        if "@" not in new_value or "." not in new_value:
            return "Invalid email format."
        record.email = new_value
        return "Email changed."

    elif field_to_change == "address":
        record.address = new_value
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
def show_contact(args, book):
    """
    show contact function
    """
   
    # Join all words in args to handle multi-word names or email inputs
    query = ' '.join(args).strip()
    
    # Attempt to find the record by name
    record = book.find(query)
    
    if record is None:
        
        # If no record is found by name, search by email
        for rec in book.data.values():  # Iterate through all records
            # Check if email exists and matches the query
            if hasattr(rec, 'email') and rec.email and str(rec.email).lower() == query.lower():
                record = rec
                break

    # If no record is found by either name or email, raise an error
    if record is None:
        raise KeyError(f"Contact not found for query: {query}")
    
    return record



@input_error
def add_birthday(args, book):
    """
    add birthday function
    """
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
    """
    show contact birthday function
    """
    name = ' '.join(args).strip()
    print(f"Looking up record for: {name}")
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found")
    return record.birthday or "No birthday set"


@input_error
def birthdays(args, book):
    """
    function to show all birthdays during input perion from starting date 
    """
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
    """
    Deletes a contact from the address book after confirming the action.

    This function first checks if the user has provided the name of the contact to delete. 
    If the contact is found in the address book, the user is asked to confirm the deletion 
    by typing 'yes' or 'no'. If the user confirms, the contact is deleted; otherwise, 
    the deletion is canceled. If the contact is not found or the user input is invalid, 
    appropriate messages are returned.

    Args:
        args (list): A list containing the contact's name as space-separated strings.
        book (AddressBook): The address book instance that contains the contacts.
    """

    if not args:
        raise ValueError("Please provide the name of the contact to delete.")
    name = " ".join(args).strip()

    # Find contact
    record = book.find(name)
    if record is None:
        return f"Contact '{name}' not found."
    
    # Ask for confirmation
    confirmation = input(f"Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
    if confirmation == "yes":
        # Remove the record from the book
        book.delete(name)
        return f"Contact '{name}' has been deleted."
    elif confirmation == "no":
        return f"Contact '{name}' was not deleted."
    else:
        return "Invalid input. Please enter 'yes' or 'no'."
