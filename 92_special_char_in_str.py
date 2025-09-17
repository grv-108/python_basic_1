# 92. Special Characters in String

# Write a Python program to define a string containing special characters in various forms.

my_str = "grv@gmail.com"

for i in my_str:
    if i in ["!", "@", "#", "$", "%", "^", "&", "*"]:
        print(f"Your string contains '{i}' special character.")