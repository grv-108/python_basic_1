# 113. Number Input Validator

# Write a Python program that inputs a number and generates an error message if it is not a number.

def getUserInput():
    return input("Enter a number : ").strip()

def numberValidator(input):
    if input.isdigit():
        return True
    else:
        return False
    
def main():
    user_input = getUserInput()
    result = numberValidator(user_input)
    print(result)
    
if __name__ == "__main__":
    main()