# Create a function that takes a datetime object as input and formats it as "Day-Month-Year" (e.g., "25-August-2023") using strftime().

# Solution :

from datetime import date, datetime

def format_date(date_obj):
    
    formatted_date = date_obj.strftime("%d-%B-%Y")
    return formatted_date
    
date_str = input("Enter a date (MM/DD/YYYY): ")
date_obj = datetime.strptime(date_str, "%m/%d/%Y")

result = format_date(date_obj)

print("The date is:", result)