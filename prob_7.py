# Create a program that takes a year and a month as input and prints the number of days in that month.
# without using calender module

# Solution:

year = int(input("Enter year:"))
month = int(input("Enter month:"))

if 1 <= month <= 12:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        print("Number of days in month is:", 31)
    elif month in [4, 6, 9, 11]:
        print("Number of days in month is:", 30)
    elif month == 2 and year % 4 == 0 :
        print("Number of days in month is:", 29)
    elif month == 2 and year % 4 != 0 :
        print("Number of days in month is:", 28)
else:
    print("Invalid month")