# Write a program that calculates the time difference between two given datetime objects and displays it in hours, minutes, and seconds.

# Solution:

from datetime import date, datetime

first_date_str = input("Enter date (e.g., MM/DD/YYYY):")
first_date_obj = datetime.strptime(first_date_str, "%m/%d/%Y")

second_date_str = input("Enter another date (e.g., MM/DD/YYYY):")
second_date_obj = datetime.strptime(second_date_str, "%m/%d/%Y")

difference = first_date_obj - second_date_obj

total_seconds = difference.total_seconds()
mins = total_seconds / 60
hourss = mins / 60

print("The Differenece between two dates is:", hourss, "hours", mins, "minutes", total_seconds, "seconds")
