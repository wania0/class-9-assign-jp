# create a current datetime and then displays it in the format "HH:MM AM/PM"

# Solution :

from datetime import datetime

dt = datetime.now()

formatted_dt = dt.strftime("%H:%M %p")

print(formatted_dt)




