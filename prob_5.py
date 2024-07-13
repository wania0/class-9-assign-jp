# Write a program that calculates and displays the number of days between two given dates.

# Solution:

from datetime import date, datetime

first_date_str = input("Enter date (e.g., MM/DD/YYYY):")
first_date_obj = datetime.strptime(first_date_str, "%m/%d/%Y")

second_date_str = input("Enter another date (e.g., MM/DD/YYYY):")
second_date_obj = datetime.strptime(second_date_str, "%m/%d/%Y")

difference = first_date_obj - second_date_obj

print("The Differenece between two dates is:", difference.days, "days")
