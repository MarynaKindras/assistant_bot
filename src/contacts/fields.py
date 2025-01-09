from datetime import datetime
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
# class Name(Field):
#     def __init__(self, value):
#         if not value:
#             raise ValueError("Name is required.")
#         super().__init__(value)

class Name(Field):
    def __init__(self, value):
        parts = value.split(maxsplit=1)
        
        self.first_name = parts[0]
        self.family_name = parts[1] if len(parts) > 1 else ""
        
        super().__init__(value)
    
    def __str__(self):
        return f"{self.first_name} {self.family_name}".strip()

class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number. It must contain exactly 10 digits.")
        
class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    
    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

class Email:
    def __init__(self, email):
        if self.validate(email):
            self.email = email
        else:
            raise ValueError("Invalid email format.")
    
    def __str__(self):
        return self.email

    def validate(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None
    
class Address:
    def __init__(self, address):
        if self.validate(address):
            self.address = address
        else:
            raise ValueError("Invalid address. Must be up to 100 characters.")
    
    def __str__(self):
        return self.address

    def validate(self, address):
        return len(address) <= 100