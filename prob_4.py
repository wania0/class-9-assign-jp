# Create a program that calculates and prints the number of days remaining until a person's next birthday.
# take users birth date as input

# Solution :

from datetime import date, datetime

birth_date_str = input("Enter your birth date (e.g., MM/DD/YYYY):")
birth_date_obj = datetime.strptime(birth_date_str, "%m/%d/%Y")

birthday_month = birth_date_obj.month
birth_day = birth_date_obj.day

current_date = date.today()
year = current_date.year
birthday = date(year,birthday_month,birth_day)

if birthday < current_date:
    birthday = date(year + 1, birthday_month, birth_day)

time_left = birthday - current_date

print("Wohooo! Only ", time_left.days, "days left in your birthday.")

