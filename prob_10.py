# Create a function that takes a datetime in the format "MM/DD/YYYY HH:MM:SS" as string  formats it as "YYYY-MM-DD HH:MM:SS".

# Solution:

from datetime import date, datetime

def format_conversion(uk_format):
    
    uk_format_obj = datetime.strptime(uk_format, "%m/%d/%Y %H:%M:%S")
    return uk_format_obj
    
uk_format = input("Enter the date in the required format (MM/DD/YYYY) H:M:S :")

iso_format_date = format_conversion(uk_format)

print("ISO Format date:", iso_format_date)
