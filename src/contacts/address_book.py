from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value in self.data:
            raise ValueError("Record with this name already exists.")
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Record not found.")
        
    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        end_date = today + timedelta(days=7)
        
        upcoming_birthdays = []
        
        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.date().replace(year=today.year)
                
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                
                if today <= birthday_this_year <= end_date:
                    if birthday_this_year.weekday() in (5, 6):
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
