# 33. Triple Sum with Equality Rule

# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

def getUserInput():
    return int(input("Enter first value : ").strip()), int(input("Enter first value : ").strip()), int(input("Enter first value : ").strip())

def main():
    a, b, c = getUserInput()
    if (a==b) or (a==c) or (b==c):
        print(f"Sum is 0")
    else:
        print(f"Sum : {a+b+c}")
        
if __name__ == "__main__":
    main()