from lib import AddressBook
from lib import Record
from lib.bot_errors import *

book = AddressBook()

def parce_input(input):
    cmd, *args = input.split()
    return cmd.lower(), *args

@error_handler
def add_contact_handler(args):
    if len(args) < 2:
        raise BotContactAddException
    name, phone = args
    if name in book.data.keys():
        raise BotContactExistsException
    record = Record(name)
    res = record.add_phone(phone)
    if res:
        return res
    book.add_record(record)
    return " Contact added."

@error_handler
def change_contact_handler(args):
    if len(args) != 2:
        raise BotContactChangeException
    name, phone = args
    if name not in book.data.keys():
        raise BotContactNotExistsException
    record = book.find(name)
    res = record.edit_phone(record.phones[0].value, phone)
    if res:
        return res
    return " Contact updated."

@error_handler
def phone_contact_handler(args):
    if len(args) != 1:
        raise BotContactPhoneException
    name = args[0]
    if name not in book.data.keys():
       raise BotContactNotExistsException
    record = book.find(name)
    return f"phones: {'; '.join(p.value for p in record.phones)}"

@error_handler
def show_all():
    for c in book.data.items():
        print(c[1])

@error_handler
def add_birthday_handler(args):
    if len(args) < 2:
        raise BotBirthdayAddException
    name, birthday = args
    if name not in book.data.keys():
        raise BotContactNotExistsException
    record = book.find(name)
    res = record.add_birthday(birthday)
    if res:
        return res
    #print(record)
    return " Birthday added."

@error_handler
def show_birthday_handler(args):
    if len(args) != 1:
        raise BotBirthdayShowException
    name = args[0]
    if name not in book.data.keys():
       raise BotContactNotExistsException
    record = book.find(name)
    return f"birthday: {record.birthday}"

@error_handler
def birthday_handler(args):
    book.get_birthdays_per_week()

if __name__ == "__main__":
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        command, *args = parce_input(user_input)

        if command in ["close", "exit"]:
            print(" Good bye!")
            break
        elif command == "hello":
            print(" How can I help you?")
        elif command == "add":
            print(add_contact_handler(args))
        elif command == "change":
            print(change_contact_handler(args))
        elif command == "phone":
            print(phone_contact_handler(args))
        elif command == "all":
            show_all()
        elif command == 'add-birthday':
            print(add_birthday_handler(args))
        elif command == 'show-birthday':
            print(show_birthday_handler(args))
        elif command == 'birthdays':
            birthday_handler(args)
        else:
            print(" Invalid command.")
