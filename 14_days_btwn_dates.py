# 14. Days Between Dates

# Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days


def getUserInput():
    return input("Enter first date : "), input("Enter sencond date : ")

# print("Enter dates in format of (day,month,year)")

# first_date, last_date = getUserInput()
# first_date = first_date.split(",")
# last_date = last_date.split(",")
# print()
# print(f"{int(last_date[0])-int(first_date[0])} days")

import datetime

f_date, l_date = getUserInput()
# print(int(f_date[0]), int(f_date[1]), int(f_date[2]))
f_date = f_date.split(",")
l_date = l_date.split(",")

f_date = datetime.date(int(f_date[0]), int(f_date[1]), int(f_date[2]))
l_date = datetime.date(int(l_date[0]), int(l_date[1]), int(l_date[2]))

delta = l_date - f_date
print(f"{delta.days} days.")