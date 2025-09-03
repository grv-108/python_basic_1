# 34. Conditional Sum to 20

# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

def getUserInput():
    return int(input("Enter first value : ").strip()), int(input("Enter second value : ").strip())

def main():
    a, b = getUserInput()
    if (a+b)>=15 and (a+b)<=20:
        print("Sum : 20")
    else:
        print(f"Sum : {a+b}")
        
if __name__ == "__main__":
    main()