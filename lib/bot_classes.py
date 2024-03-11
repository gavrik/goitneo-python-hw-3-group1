from collections import UserDict
from datetime import datetime
from lib.birthday import get_birthdays_per_week
from lib.bot_errors import *

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        Field.__init__(self, name)

class Phone(Field):
    def __init__(self, value):
        if len(value) < 10:
            raise BotPhoneLenghtException
        Field.__init__(self, value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    @error_handler
    def add_phone(self, phone):
        self.phones.append(
            Phone(phone)
        )

    @error_handler
    def add_birthday(self, value):
        self.birthday = Birthday(value)
    
    @error_handler
    def edit_phone(self, pold, pnew):
        for p in range(len(self.phones)):
            if self.phones[p].value == pold:
                self.phones[p] = Phone(pnew)
    
    def find_phone(self, value):
        for p in self.phones:
            if p.value == value:
                return p
        return None # Empty Phone object expected

    def remove_phone(self, value):
        p = self.find_phone(value)
        if p is not None:
            self.phones.remove(p)

    def __str__(self):
        return f"  Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"
    
    def __call__(self):
        return self.name.value

class Birthday(Field):
    def __init__(self, value):
        try:
            Field.__init__(self, datetime.strptime(value, '%d.%m.%Y'))
        except ValueError:
            raise BotBirthdayWrongFormat
    def __str__(self):
        return self.value.strftime('%d.%m.%Y') 

class AddressBook(UserDict):
    def add_record(self, value):
        self.data[value()] = value
    
    def __find(self, value):
        try:
            return self.data[value]
        except:
            raise BotRecordNotFoundException

    @error_handler
    def find(self, value):
        return self.__find(value)

    @error_handler
    def delete(self, value):
        self.__find(value)
        del self.data[value]
    
    def get_birthdays_per_week(self):
        d = []
        for i in self.data.items():
            d.append(
                {"name": i[1].name.value, "birthday": i[1].birthday.value}
            )
        get_birthdays_per_week(d)

if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    #john_record.add_phone("0987654321")
    #john_record.add_phone("0987654")
    john_record.add_phone("5555555555")
    john_record.add_birthday('03.04.2024')
    #print(john_record)

    book.add_record(john_record)
    #print(book.data)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_birthday("2024.04.04")
    book.add_record(jane_record)

    #print(jane_record)
    #print(book.data)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")
    #john.remove_phone("5555555555")
    #print(john)
    book.delete("Jane")

    #lev = book.find('Lev')
    #book.delete("Lev")

    #print(book.data)
