# 124. Variable Equality Checker

# Write a Python program to check whether multiple variables have the same value.

def getUserInput():
    return int(input("Enter a : ").strip()), int(input("Enter c : ").strip()), int(input("Enter c : ").strip())

def main():
    a, b, c = getUserInput()
    
    if a == b == c:
        print("All variable have same value.")
    else:
        print("No!!!")
        
if __name__ == "__main__":
    main()