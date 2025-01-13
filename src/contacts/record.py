"""
This module defines a `Record` class that represents a contact in an address book. 
A `Record` includes various fields such as name, phone numbers, birthday, email, 
and address, along with methods to manage and modify these fields. 

The class relies on several other classes such as `Name`, `Phone`, `Birthday`, 
`Address`, and `Email`, which are imported from the `src.contacts.fields` module. 

The `Record` class allows the addition, deletion, modification, and retrieval of 
contact information, providing a comprehensive way to manage individual contacts 
within an address book.

The methods in this class provide functionality to:
- Add and delete phone numbers.
- Edit and search for specific phone numbers.
- Add and update birthday, email, and address information.
- Find a contact based on the name or email.
- Display the contact's full details in a readable format.

The `Record` class is designed to work with other classes, such as `AddressBook`, 
which handles the collection of multiple `Record` instances.

Attributes:
    name (Name): The Name object representing the contact's name.
    phones (list): A list to store `Phone` objects associated with the contact.
    birthday (Birthday or None): The contact's birthday as a `Birthday` object, if set.
    email (Email or None): The contact's email address as an `Email` object, if set.
    address (Address or None): The contact's address as an `Address` object, if set.

Methods:
    - __init__(name): Initializes a contact record with the given name.
    - add_phone(phone): Adds a new phone number to the contact.
    - delete_phone(phone): Removes an existing phone number from the contact.
    - edit_phone(old_phone, new_phone): Edits an existing phone number.
    - find_phone(phone): Finds a phone number in the contact's list.
    - find(query): Finds a contact by name or email.
    - show_contact(args, book): Displays a contact's details from the address book.
    - add_birthday(birthday): Sets or updates the contact's birthday.
    - add_email(email): Sets or updates the contact's email.
    - add_address(address): Sets or updates the contact's address.
    - __str__(): Returns a string representation of the contact record.

Dependencies:
    - Name: Represents the contact's name (first and last).
    - Phone: Represents the contact's phone number.
    - Birthday: Represents the contact's birthday.
    - Address: Represents the contact's physical address.
    - Email: Represents the contact's email address.
"""
from src.contacts.fields import Name, Phone, Birthday, Address, Email

class Record:
    """
    Record
    Attributes:
        name (Name): The Name object representing the contact's name.
        phones (list): An empty list to store Phone objects.
        birthday (None): Placeholder for a Birthday object.
        email (None): Placeholder for an Email object.
        address (None): Placeholder for an Address object.
    """

    def __init__(self, name):
        """
        Initializes a Record instance with the contact's name.

        Args:
        name (str): The name of the contact.
        """
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    def add_phone(self, phone):
        """
        Adds a phone number to the contact.

        Args:
            phone (str): The phone number to add.

        Raises:
            ValueError: If the phone number is invalid.
        """
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        """
        Removes a phone number from the contact.

        Args:
            phone (str): The phone number to remove.

        Raises:
            ValueError: If the phone number does not exist in the record.
        """
        phone_to_remove = None
        for p in self.phones:
            if p.value == phone:
                phone_to_remove = p
                break
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError("Phone not found.")

    def edit_phone(self, old_phone, new_phone):
        """
        Edits an existing phone number by replacing it with a new phone number.

        Args:
            old_phone (str): The old phone number to be replaced.
            new_phone (str): The new phone number to replace the old one.

        Raises:
            ValueError: If the old phone number is not found in the contact's phone list.
            ValueError: If the new phone number is invalid (not 10 digits or contains non-numeric characters).
        """
        for p in self.phones:
            if p.value == old_phone:
                Phone.validate(new_phone)
                p.value = new_phone
                return
        raise ValueError("Phone not found.")

    def find_phone(self, phone):
        """
        Searches for a phone number in the contact's list of phone numbers.

        Args:
            phone (str): The phone number to search for.

        Returns:
            Phone or None: If the phone number is found, the corresponding Phone object is returned. 
                            If the phone number is not found, None is returned.

        Prints:
            The phone object if found.

        """
        for p in self.phones:
            if p.value == phone:
                print(p)
                return p
        return None
    
    def show_contact(self, args, book):
        """
        Displays the details of a contact by searching for the provided name.

        Args:
            args (list): A list containing the contact's name as space-separated strings.
            book (AddressBook): The address book instance containing the contacts.

        Returns:
            str: A string with the contact's details such as name, phones, birthday, email, and address. 
                If the contact is not found, returns a message indicating so.
        """
        name = " ".join(args).strip()
        record = book.find(name)
        if not record:
            return f"Contact '{name}' not found."
        phones = "; ".join(p.value for p in record.phones) if record.phones else "No phone numbers set"
        email = record.email if record.email else "Not provided"
        address = record.address if record.address else "Not provided"
        birthday = record.birthday if record.birthday else "Not set"
        return (f"Contact name: {record.name.value}, phones: {phones}, "
                f"birthday: {birthday}, email: {email}, address: {address}")
    
    def add_birthday(self, birthday):
        """
        Adds/Updates the contact's birthday.

        Args:
            birthday (str): The birthday in the format "DD.MM.YYYY".

        Raises:
            ValueError: If the birthday format is invalid.
        """
        self.birthday = Birthday(birthday)

    def add_email(self, email):
        """
        Adds/Updates the contact's email address.

        Args:
            email (str): The email address to update.

        Raises:
            ValueError: If the email format is invalid.
        """
        self.email = Email(email)

    def add_address(self, address):
        """
        Adds/Updates the contact's physical address.

        Args:
            address (str): The address to update.

        Raises:
            ValueError: If the address is invalid.
        """
        self.address = Address(address)

    def __str__(self):
        """
        Returns a string representation of the contact record.

        Returns:
            str: A summary of the contact's details, including name, phones, birthday, email, and address.
        """
        phones = '; '.join(p.value for p in self.phones)
        birthday = f"birthday: {self.birthday}" if self.birthday else "no birthday set"
        address = f"address: {getattr(self, 'address', 'no address set')}"
        email = f"email: {getattr(self, 'email', 'no email set')}"

        return f"Contact name: {self.name.value}, phones: {phones}, {birthday}, {email}, {address}"