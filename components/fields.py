from abc import ABC,abstractmethod
from datetime import datetime

class Field(ABC):
    @abstractmethod
    def __init__(self, value):
        ...
  
class Name(Field):
    def __init__(self, value:str):
        self.value=value

class Phone(Field):
    def __init__(self, value: str): 

        if value.isdigit() and len(value) == 10:
            self.value=value
        else:
            raise ValueError(f"Phone is too short: {value}. Please put in 10 digits")

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
