import pickle
import json

from components.addressbook import AddressBook



def save_data(book, filename="addressbook.json"):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump({"contacts":book.to_dict()}, file, ensure_ascii=False, indent=4)

def load_data(filename="addressbook.json"):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return AddressBook.from_dict(data['contacts'])
    except FileNotFoundError:
        return AddressBook()
    

# def load_data(filename="addressbook.pkl"):
#     try:
#         with open(filename, "rb") as f:
#             return pickle.load(f)
#     except FileNotFoundError:
#         return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено

# def save_data(book, filename="addressbook.pkl"):
#     with open(filename, "wb") as f:
#         pickle.dump(book, f)