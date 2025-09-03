# 16. Difference from 17

# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

def getUserInput():
    return int(input("Enter number : "))

num = getUserInput()
if num > 17:
    temp = abs(17-num) * 2
if num < 17:
    temp = abs(17 - num)
    print(temp)
