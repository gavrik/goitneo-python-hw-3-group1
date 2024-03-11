class BotContactExistsException(Exception):
    pass

class BotContactNotExistsException(Exception):
    pass

class BotContactAddException(Exception):
    pass

class BotContactChangeException(Exception):
    pass

class BotContactPhoneException(Exception):
    pass

class BotPhoneLenghtException(Exception):
    pass

class BotRecordNotFoundException(Exception):
    pass

class BotBirthdayWrongFormat(Exception):
    pass

class BotBirthdayAddException(Exception):
    pass

class BotBirthdayShowException(Exception):
    pass

def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "  Error: Wrong syntax!"
        except BotContactExistsException:
            return "  Contact is present in DB. Use change command instead"
        except BotContactNotExistsException:
            return "  Contact is not present in DB"
        except BotContactAddException:
            return "  Error: Wrong syntax!\n  Example: add UserName 12345678890"
        except BotContactChangeException:
            return "  Error: Wrong syntax!\n  Example: change UserName 12345678890"
        except BotContactPhoneException:
            return "  Error: Wrong syntax!\n  Example: phone UserName"
        except BotBirthdayWrongFormat:
            return "  Wrong birthday date format\n  Example: DD.MM.YYYY (03.04.2024)"
        except BotPhoneLenghtException:
            return "  Wrong phone lenght"
        except BotRecordNotFoundException:
            return "  Record not found"
        except BotBirthdayAddException:
            return "  Error: Wrong syntax!\n  Example: add-birthday UserName 03.04.2024"
        except BotBirthdayShowException:
            return "  Error: Wrong syntax!\n  Example: show-birthday UserName"
        except Exception as e:
            return f"  Something happen! {e}"
    return inner
