# Create a function that takes a timezone name and a number of hours as input, and prints the current time plus the specified hours in that timezone

# Solution :

from datetime import datetime, date, timedelta
import pytz

def added_hours(tz_name, hours_to_add):
    
    dt = datetime.now()
    target_time = dt + timedelta(hours=hours_to_add)
    
    tz = pytz.timezone(tz_name)
    localize_dt = tz.localize(target_time)

    print("After adding two hours time becomes", localize_dt)
    
added_hours("Asia/Karachi", 2)