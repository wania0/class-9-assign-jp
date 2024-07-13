# Create a function that takes a datetime object and a number of hours as input, then returns a new datetime object with the added hours.

# Solution:

from datetime import datetime, timedelta

def hours_added(str_date, added_hours):
    
    str_date_obj = datetime.strptime(str_date, "%m/%d/%Y %H:%M:%S")
    new_date = str_date_obj + timedelta(hours = added_hours)
    
    return new_date
    
    
str_date = input("Enter the starting date (MM/DD/YYYY %H:%M:%S):")
added_hours = int(input("Enter the number of hours you wanna add:"))

updated_date = hours_added(str_date, added_hours)

print("The Updated date and time is:", updated_date)