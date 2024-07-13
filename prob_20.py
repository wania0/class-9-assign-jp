# Create a function that takes a datetime object as input and displays the day of the week (e.g., "Monday") using strftime().
# hint: https://strftime.org/

# Solution :

from datetime import datetime

def day_of_week(dt_obj):
    
    day_name = dt_obj.strftime("%A")
    return day_name    

str_date = input("Enter the date in (MM/DD/YYYY) format:")
dt_obj = datetime.strptime(str_date, "%m/%d/%Y")

dayy = day_of_week(dt_obj)

print("Today is", dayy)