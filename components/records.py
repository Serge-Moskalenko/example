from components.fields import Phone,Name,Birthday


class Record:
    def __init__(self, name, phones=None, birthday=None):
        self.name = Name(name)
        self.phones = phones if phones else []
        self.birthday = birthday

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        birthday = f", birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones}{birthday}"
    
    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError as e:
            print(e)

    def add_birthday(self, date):
        try:
            self.birthday = Birthday(date)
        except ValueError as e:
            print(e)

    def edit_phone(self, old_phone, new_phone):
        try:
            for phone in self.phones:
                if phone.value == old_phone:
                    phone.value = Phone(new_phone).value
                    break
            else:
                raise ValueError('Phone not found')
        except ValueError as e:
            print(e)

    def delete_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def to_dict(self):
        return {
            "name": self.name.value,
            "phones": [p.value for p in self.phones],
            "birthday": self.birthday.value.strftime("%d.%m.%Y") if self.birthday else None
        }

    @classmethod
    def from_dict(cls, data):
        name = data['name']
        phones = [Phone(phone) for phone in data['phones']]
        birthday = Birthday(data['birthday']) if data['birthday'] else None
        return cls(name, phones, birthday)