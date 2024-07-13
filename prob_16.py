# create a datetime object from the string "08-26-2023 08:10:00 PM"
# hint: https://strftime.org/


from datetime import datetime

date_str = "08-26-2023 08:10:00 PM"
date_obj = datetime.strptime(date_str, "%m-%d-%Y %I:%M:%S %p")

formatted_date = date_obj.strftime("%m-%d-%Y %I:%M:%S %p")

print("The formatted date is:", formatted_date)