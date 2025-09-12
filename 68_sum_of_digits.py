# 68. Sum of Digits

# Write a Python program to calculate sum of digits of a number.

def getUserInput():
    return int(input("Enter a digit --> ").strip())

def main():
    digit = getUserInput()
    temp = 0
    while len(digit) != 0:
        