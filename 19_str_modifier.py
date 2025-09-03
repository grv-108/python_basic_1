# 19. Prefix "Is" String Modifier

# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".

def getUserInput():
    return input("Enter string : ")

user_input = getUserInput()

if user_input.startswith("is") or user_input.startswith("Is"):
    print(user_input)
else:
    print(f"Is {user_input}")