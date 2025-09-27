# 147. Divisibility Tester

# Write a Python function to check whether a number is divisible by another number. Accept two integer values from the user.

def getUserInput():
    return int(input("Enter Number : ").strip()), int(input("Enter divisor : ").strip())

def logic(a, b):
    while a >= b:
        if a % b == 0:
            return True
        else:
            return False
    else:
        return False
    
def main():
    a, b = getUserInput()
    result = logic(a, b)
    
    print(result)
    
if __name__ == "__main__":
    main()