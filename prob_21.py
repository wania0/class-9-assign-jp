# Create a function that takes a timezone name as input and prints the current date time object in that timezone.

# Solution :

from datetime import datetime
import pytz

def check_timezone(timezone_name):
    
    utc_time = datetime.now(pytz.utc)
    target_timezone = pytz.timezone(timezone_name)
    target_time = utc_time.astimezone(target_timezone)
    
    print("The current date and time in", timezone_name, "is", target_time)

check_timezone('Asia/Karachi')
