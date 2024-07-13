# Create a program that takes a date as string and returns the corresponding day of the week (e.g., Monday, Tuesday, etc.).

# Solution :

from datetime import date, datetime

datee = input("Enter date (e.g., MM/DD/YYYY):")
datee_obj = datetime.strptime(datee, "%m/%d/%Y")

day_name = datee_obj.strftime("%A")
print("The name of day is:", day_name)
