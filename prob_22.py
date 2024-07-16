# Write a program that converts a given date time (tz aware) string from one timezone to another.

# Solution:

from datetime import datetime, date
import pytz

tz_aware_dt_str = "2024-07-16 17:23:36.045782+03:00"
tz_aware_dt_obj = datetime.fromisoformat(tz_aware_dt_str)

convert_tz = pytz.timezone("Asia/Kolkata")
print("The date and time of kolkata is:", tz_aware_dt_obj.astimezone(convert_tz))

