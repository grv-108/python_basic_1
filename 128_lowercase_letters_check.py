# 128. Lowercase Letters Checker

# Write a Python program to check whether lowercase letters exist in a string.

my_str = "THIS IS MY STRINg"

print(any(c.islower() for c in my_str))