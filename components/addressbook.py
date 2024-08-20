from collections import UserDict
from datetime import datetime, timedelta

from components.records import Record

class AddressBook(UserDict):
    def __str__(self):
        return '\n'.join(str(contact) for contact in self.data.values())
    
    def add_record(self, contact):
        self.data[contact.name.value] = contact

    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []
        
        for item in self.data.values():
            if item.birthday:
                birthday_this_year = item.birthday.value.replace(year=today.year)
                days_until_birthday = (birthday_this_year - today).days
                
                if 0 <= days_until_birthday <= 7:
                    if birthday_this_year.weekday() == 5:  
                        birthday_this_year += timedelta(days=2)
                    elif birthday_this_year.weekday() == 6:
                        birthday_this_year += timedelta(days=1)

                    upcoming_birthdays.append({
                        "name": item.name.value,
                        "birthday": birthday_this_year
                    })

        return upcoming_birthdays

    def to_dict(self):
        return {name: record.to_dict() for name, record in self.data.items()}

    @classmethod
    def from_dict(cls, data):
        ab = cls()
        for name, record_data in data.items():
            ab.add_record(Record.from_dict(record_data))
        return ab