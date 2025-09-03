# 18. Triple Sum Calculator

# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

def getUserInput():
    return int(input("Enter 1 num : ")), int(input("Enter 2 num : ")), int(input("Enter 3 num : "))

a, b, c = getUserInput()
if a == b == c:
    print((a + a + a) * 3)
else:
    print(a + b + c)