# 48. String to Numeric Parser

# Write a Python program to parse a string to float or integer.

def getUserInput():
    return input("Enter digit : ").strip()

def main():
    user_input = getUserInput()
    user_input = float(user_input)
    print(f"User input to int : {user_input}")
    user_input = int(user_input)
    print(f"User input to int : {user_input}")

if __name__ == "__main__":
    main()