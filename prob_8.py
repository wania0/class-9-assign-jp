# Create a function that takes a starting date and a number of days as input, and then calculates and prints the date that is the specified number of days in the future.

# Solution:

from datetime import datetime, timedelta

def calculate_future_date(starting_date, number_of_days):
    
    starting_date_obj = datetime.strptime(starting_date, "%m/%d/%Y")
    future_date_obj = starting_date_obj + timedelta(days = number_of_days)
    
    return future_date_obj
    
    
starting_date = input("Enter the starting date (MM/DD/YYYY): ")
number_of_days = int(input("Enter the number of days you wanna add: "))

future_date = calculate_future_date(starting_date, number_of_days)

print("Total days are:", future_date.day, "days")