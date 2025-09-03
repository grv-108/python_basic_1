# 17. Number Range Tester

# Write a Python program to test whether a number is within 100 of 1000 or 2000.

def getUserInput():
    return int(input("Enter number : ").strip())

num = getUserInput()

if ((num >= 1000) and (num <= 1100)) or ((num >= 2000) and (num <= 2100)):
    print("Yes!!!")
else:
    print("No!!!")