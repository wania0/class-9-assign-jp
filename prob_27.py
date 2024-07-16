# Design a program that helps schedule a meeting across different timezones. The program should take the meeting time in one timezone and display the corresponding times in other timezones.
# consider three countries: UK, US, Saudi Arab and Pakistan
# consider the meeting time is: 30 August 2023 at 2 PM Pakistan time

# Solution :

from datetime import datetime
import pytz

meeting_time_str = "2023-08-30 14:00:00"  

meeting_time_obj = datetime.strptime(meeting_time_str, "%Y-%m-%d %H:%M:%S")

pak_tz = pytz.timezone("Asia/Karachi")

pak_tz_localize = pak_tz.localize(meeting_time_obj)
print("Meeting time in Pakistan (Asia/Karachi):", pak_tz_localize)

uk_tz = pytz.timezone("Europe/London")
dt_in_uk = pak_tz_localize.astimezone(uk_tz)
print("Meeting time in UK (Europe/London):", dt_in_uk)

us_eastern_tz = pytz.timezone("US/Eastern")
dt_in_us_eastern = pak_tz_localize.astimezone(us_eastern_tz)
print("Meeting time in US (Eastern Time):", dt_in_us_eastern)

us_tz = pytz.timezone("US/Central")
dt_in_us = pak_tz_localize.astimezone(us_tz)
print("Meeting time in US (Central Time):", dt_in_us)

us_pacific_tz = pytz.timezone("US/Pacific")
dt_in_us_pacific = pak_tz_localize.astimezone(us_pacific_tz)
print("Meeting time in US (Pacific Time):", dt_in_us_pacific)

saudi_tz = pytz.timezone("Asia/Riyadh")
dt_in_saudi = pak_tz_localize.astimezone(saudi_tz)
print("Meeting time in Saudi Arabia (Asia/Riyadh):", dt_in_saudi)
