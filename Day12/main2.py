import datetime
this_year = datetime.datetime.today().year


def age_in_minutes(b_year: int):
    d1 = datetime.datetime.strptime(f'{this_year}', '%Y')
    d2 = datetime.datetime.strptime(f'{b_year}', '%Y')
    age = (d1-d2).days * 24 * 60
    return f"{age:,}"


while True:
    birth_year = input("Enter you birth year: ")
    try:
        if int(birth_year) == this_year:
            print("Please enter year less than this year...")
        elif int(birth_year) > this_year:
            print("Please enter year less than this year...")
        elif len(birth_year) < 4 or len(birth_year) > 5:
            print("PLease enter a valid year...")
        elif int(birth_year) <= 1900:
            print("Please enter a year after 1900...")
        else:
            minutes_old = age_in_minutes(int(birth_year))
            print(f"You are {minutes_old} minutes old.")
            break
    except ValueError:
        print("Please enter in a year format: ")
