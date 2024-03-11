from datetime import datetime

weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def get_birthdays_per_week(users):
    #print(users)
    res = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    now = datetime.today().date()
    
    for u in users:
        name = u["name"]
        birthday = u["birthday"].date()
        birthday_this_year = birthday.replace(year = now.year)
        if birthday_this_year < now:
            birthday_this_year = birthday_this_year.replace(year = birthday_this_year.year + 1)

        delta_days = (birthday_this_year - now).days
        if delta_days < 7:
            week_index = int(datetime.strftime(birthday, '%w'))
            #print(week_index)
            res[weeks[ week_index if week_index not in [5,6] else 0 ]].append(name)


    for i in res:
        if len(res[i]) < 1:
            continue
        print("{}: {}".format(i, ", ".join(res[i])))

    return res


if __name__ == "__main__":
    users = [
       {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
       {"name": "Bill Gates1", "birthday": datetime(1955, 3, 18)},
       {"name": "Bill Gates2", "birthday": datetime(1955, 3, 19)},
       {"name": "Bill Gates3", "birthday": datetime(1955, 3, 22)},
       {"name": "Bill Gates4", "birthday": datetime(1955, 3, 24)},
       {"name": "Bill Gates5", "birthday": datetime(1955, 3, 21)},
       {"name": "Bill Gates6", "birthday": datetime(1955, 3, 17)},
       {"name": "Bill Gates7", "birthday": datetime(1955, 3, 15)}

    ]
    
    get_birthdays_per_week(users)
