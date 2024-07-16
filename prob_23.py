# Write a program that takes a datetime object (naive) and a timezone name as input, and returns a localized datetime object in the specified timezone.

# Solution:

from datetime import datetime, date
import pytz

dt_input_str = input("Enter date in the format (YYYY-MM-DDTHH:MM:SS)")

naive_dt_input_obj = datetime.fromisoformat(dt_input_str)

time_zone_name = input("Enter the timezone name:")

aware_dt = pytz.timezone(time_zone_name)

print("Localized datetime in the desired timezone is:", aware_dt.localize(naive_dt_input_obj))