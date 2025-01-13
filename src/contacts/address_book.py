"""
AddressBook class built on top of Python's UserDict class. 
It provides functionality to store, retrieve, update, and delete contact records, 
as well as manage additional features like searching, 
displaying upcoming birthdays, and showing all contacts
"""
from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    """
    The AddressBook class serves as a container for managing contact records
    """
    def add_record(self, record):
        """
        Adds a contact record to the address book.

        Checks if a record with the same name already exists. If it does, a ValueError is raised.
        Otherwise, the record is added to the address book's data.

        Args:
            record (Record): The contact record to be added to the address book.

        Raises:
            ValueError: If a record with the same name already exists in the address book.
        """
        if record.name.value in self.data:
            raise ValueError("Record with this name already exists.")
        self.data[record.name.value] = record


    def find(self, query):
        """
        Searches for a contact record based on the provided query (either name or email).

        Args:
            query (str): The name or email of the contact to search for.

        Returns:
            Record or None: If the contact is found, the corresponding Record object is returned.
                            If no match is found, None is returned.
        """
        # Find a record by query
        return self.data.get(query)

    def delete(self, name):
        """
        Deletes a contact record from the address book by name.

        Checks if a record with the specified name exists in the address book. 
        If the record is found, it is deleted. If not, a ValueError is raised.

        Args:
            name (str): The name of the contact to be deleted.

        Raises:
            ValueError: If no contact record with the given name is found.
        """
        # Check if the contact exists in the address book
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Record not found.")
        
    def get_upcoming_birthdays(self, days):
        """
        this function shows all upcoming birthdays from address.book buding perion entered in the input
        """
        today = datetime.today().date()
        end_date = today + timedelta(days=days)

        upcoming_birthdays = []

        for record in self.data.values():
            # Ensure the record has a valid birthday value
            if not (hasattr(record, 'birthday') and record.birthday and record.birthday.value):
                continue  # Skip records without a valid birthday

            # Calculate the birthday for this year
            birthday_date = record.birthday.value.date()
            birthday_this_year = birthday_date.replace(year=today.year)

            # If the birthday has already passed this year, use next year's date
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            # Check if the birthday falls within the specified range
            if today <= birthday_this_year <= end_date:
                # Adjust the congratulation date if it falls on a weekend
                if birthday_this_year.weekday() in (5, 6):  # Saturday or Sunday
                    days_to_monday = (7 - birthday_this_year.weekday()) % 7
                    congratulation_date = birthday_this_year + timedelta(days=days_to_monday)
                else:
                    congratulation_date = birthday_this_year

                upcoming_birthdays.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })

        return upcoming_birthdays

    
    def display_all_contacts(self):
        """
        function shows all contacts
        """
        if not self.data:
            print("The address book is empty.")
        if not hasattr(self, 'email'):
            self.email = None
        if not hasattr(self, 'address'):
            self.address = None 
        else:
            print("All contacts:")
            for record in self.data.values():
                print(record)