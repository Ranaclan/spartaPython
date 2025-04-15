from datetime import datetime
from datetime import date

name_str = input("What is your name? ")
age_int = int(input("What is your age? "))
day = int(input("What day were you born? " ))
month = int(input("What month were you born? " ))

currentYear = datetime.now().year
year = currentYear - age_int
born = date(year, month, day)
daysLived = (date.today() - born).days
hoursLived = daysLived * 24
print(f"OMG, you are {age_int} years old so you were born in {year}, so have lived for {hoursLived} hours")

birthday = date(currentYear, month, day)
if date.today() > birthday:
    print("Your birthday has already passed this year")
else:
    print("Your birthday this year is yet to come")
