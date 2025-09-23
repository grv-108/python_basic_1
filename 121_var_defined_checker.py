# 121. Variable Defined Checker

# Write a Python program to determine if a variable is defined or not.

try:
    x = 4
except NameError:
    print("Variable is not defined!")
else:
    print("Variable is defined.")
    
try:
    y
except NameError:
    print("Variable is not defined!")
else:
    print("Variable is defined.")