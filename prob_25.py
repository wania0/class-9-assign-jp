# Write a program that calculates the date and time of the daylight saving start in the year 2022.
# take timezone "US/Pacific"
# take string date as "2022-01-01 00:00:00"
# hint: use
# bool(tz_aware_dt.dst()) == True # dst activated
# bool(tz_aware_dt.dst()) == False # dst not activated

# Solution :

from datetime import datetime, date, timedelta
import pytz

time_zone = pytz.timezone("US/Pacific")
starting_date_str = "2022-01-01 00:00:00"
starting_date_obj = datetime.strptime(starting_date_str, "%Y-%m-%d %H:%M:%S")
localize_dt = time_zone.localize(starting_date_obj)
print(localize_dt)
