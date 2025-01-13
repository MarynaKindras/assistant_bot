"""
This module provides a framework for managing contact information. 
It defines several classes to represent different fields of a contact record, 
including Field, Name, Phone, Birthday, Email, and Address. 
Each class encapsulates specific validation rules and behaviors for its respective field
"""
from datetime import datetime
import re

class Field:
    """
    Represents a generic field in a contact record.

    Attributes:
        value (str): The value of the field, which must be a string of up to 255 characters.
    """
    def __init__(self, value):
        """
        Initializes a Field instance with a given value.

        Args:
            value (str): The value to be stored in the field.

        Raises:
            ValueError: If the value exceeds 255 characters or is not a string.
        """
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """
    Represents a name field for a contact, consisting of a first name and optionally a family name.

    Attributes:
        first_name (str): The first name of the contact.
        family_name (str): The family name of the contact, defaulting to an empty string if not provided.
    """
    def __init__(self, value):
        """
        Initializes a Name instance with a given value.

        The value is split into first and family name. If only one name is provided, it is stored as the first name.

        Args:
            value (str): The full name of the contact, with parts separated by a space.

        Raises:
            ValueError: If the name value is empty, exceeds 255 characters, or is not a string.
        """
        parts = value.split(maxsplit=1)
        
        self.first_name = parts[0]
        self.family_name = parts[1] if len(parts) > 1 else ""
        super().__init__(value)
    
    def __str__(self):
        """
        Returns the string representation of the name.

        Returns:
            str: The concatenated first name and family name.
        """
        return f"{self.first_name} {self.family_name}".strip()

class Phone(Field):
    """
    Represents a phone number field for a contact.

    A phone number must be exactly 10 digits long and contain only numeric characters.

    Attributes:
        value (str): The phone number value as a string.
    """
    def __init__(self, value):
        """
        Initializes a Phone instance after validating the phone number.

        Args:
            value (str): The phone number to be assigned to the contact.

        Raises:
            ValueError: If the phone number is invalid (not 10 digits or contains non-numeric characters).
        """
        self.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value):
        """
        Validates the phone number.

        A valid phone number must:
        - Contain exactly 10 digits.
        - Be entirely numeric.

        Args:
            value (str): The phone number to validate.

        Raises:
            ValueError: If the phone number does not meet validation criteria.
        """
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number. It must contain exactly 10 digits.")
        
class Birthday(Field):
    """
    Represents a birthday field for a contact.
    The birthday must be in the format "DD.MM.YYYY" and will be stored as a datetime object.
    Attributes:
        value (datetime): The parsed date of birth.
    """
    def __init__(self, value):
        """
        Initializes a Birthday instance after validating and parsing the date.

        Args:
            value (str): The birthday in the format "DD.MM.YYYY".

        Raises:
            ValueError: If the date is not in the correct format or is invalid.
        """
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    
    def __str__(self):
        """
        Returns the birthday as a string in the format "DD.MM.YYYY".

        Returns:
            str: The birthday formatted as a string.
        """
        return self.value.strftime("%d.%m.%Y")

class Email:
    """
    Represents the email address of a contact.

    Attributes:
        value (str): The email address as a string.
    """
    def __init__(self, email):
        """
        Initializes an Email instance with a given email address.

        Args:
            value (str): The email address.
        """
        if self.validate(email):
            self.email = email
        else:
            raise ValueError("Invalid email format.")
    
    def __str__(self):
        return self.email

    def validate(self, email):
        """
        Validate the email to be sure is it real
        """
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None
    
class Address:
    """
    Represents the address of a contact.

    Attributes:
        value (str): The address as a string, multi-words, limited to 100 characters.
    """
    def __init__(self, address):
        # Validate the address
        if self.validate(address):
            self.address = address.strip()  # Remove leading/trailing whitespace
        else:
            raise ValueError("Invalid address. Must be up to 100 characters.")
    
    def __str__(self):
        return self.address

    @staticmethod
    def validate(address):
        """
        Validates the address to ensure it is a string of up to 100 characters.
        :param address: The address to validate.
        :return: True if valid, False otherwise.
        """
        return isinstance(address, str) and len(address.strip()) <= 100