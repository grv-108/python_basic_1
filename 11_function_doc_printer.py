# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.

import builtins

def getUserInput():
    return input("Enter function name : ").strip()

user_input = getUserInput()

if hasattr(builtins, user_input):
    func = getattr(builtins, user_input)
    print(func.__doc__)
else:
    print("Invalid build-in function name.")
    