# 20. String Copy Generator

# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

def getUserInput():
    return input("Enter string : ").strip(), int(input("How many times you want copy of this string : ").strip())

user_str, num = getUserInput()

print(" ".join([user_str] * 3))