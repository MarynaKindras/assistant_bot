from .fields import Name, Phone, Birthday, Address, Email

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
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
        for p in self.phones:
            if p.value == old_phone:
                Phone.validate(new_phone)
                p.value = new_phone
                return
        raise ValueError("Phone not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                print(p)
                return p
        return None
    
    # def find(self, name):
    #     return self.records.get(name) 
    def find(self, query):
    # Find a record by name
        return self.data.get(query)
    
    def show_contact(args, book):
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

    # def find(self, query):
    
    #     query = query.lower().strip()

    #     for record in self.records.values():
    #     # Match by name
    #         if record.name.value.lower() == query:
    #             return record

    #     # Match by email
    #     if record.email and record.email.lower() == query:
    #         return record

    #     # Match by phone number
    #     for phone in record.phones:
    #         if phone.value == query:
    #             return record

    # If no match is found
        # return None
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_email(self, email):
        self.email = Email(email)

    def add_address(self, address):
        self.address = Address(address)

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        birthday = f"birthday: {self.birthday}" if self.birthday else "no birthday set"
        address = f"address: {getattr(self, 'address', 'no address set')}"
        email = f"email: {getattr(self, 'email', 'no email set')}"

        return f"Contact name: {self.name.value}, phones: {phones}, {birthday}, {email}, {address}"