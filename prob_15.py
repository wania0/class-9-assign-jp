# create a datetime object from the string "26-08-2023 15:18:33.983780-07:00" 
# hint: https://strftime.org/

# Solution :

from datetime import datetime

date_str = "26-08-2023 15:18:33.983780-07:00"
date_obj = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S.%f%z")


print("Datetime object:", date_obj)

