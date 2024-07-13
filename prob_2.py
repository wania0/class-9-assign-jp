# Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".

# Solution :

from datetime import datetime

input_date = "07/08/2024"

iso_format = datetime.strptime(input_date, "%m/%d/%Y")

iso_format_date = datetime.date(iso_format)

print("The date in iso format is:", iso_format_date)


