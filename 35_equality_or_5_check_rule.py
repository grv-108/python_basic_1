# 35. Equality or 5 Rule Checker

# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

def getUserInput():
    return int(input("Enter first value : ").strip()), int(input("Enter second value : ").strip())

def main():
    a, b = getUserInput()
    if (a==b) or ((a+b) == 5) or ((a-b) == 5):
        print(True)
    else:
        print(False)
        
if __name__ == "__main__":
    main()