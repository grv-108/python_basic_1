# 36. Add Integers Validator

# Write a Python program to add two objects if both objects are integers.

def getUserInput():
    return int(input("Enter first value : ").strip()), int(input("Enter first value : ").strip())

def main():
    try:
        a, b = getUserInput()
        if not isinstance(a, int) and not isinstance(b, int):
            print("Invalid User Input!!!")
        else:
            print(a+b)
    except ValueError:
        print("Invalid input.\nUser didn't enter integer value.")
        
if __name__ == "__main__":
    main()