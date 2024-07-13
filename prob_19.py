# Write a program that takes a user-entered date in the format "MM/DD/YYYY" and prints it in the format "YYYY-MM-DD".

# Solution :

from datetime import datetime

str_dt = input("Enter date in (MM/DD/YYYY) format:")

dt_obj = datetime.strptime(str_dt, "%m/%d/%Y")

formatted_date = dt_obj.strftime("%Y-%m-%d")

print(formatted_date)
