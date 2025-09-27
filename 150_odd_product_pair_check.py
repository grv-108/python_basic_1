# 150. Odd Product Pair Checker

# Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence of integer values.

def getUserInput():
    return int(input("Enter a number : ").strip()), int(input("Enter second number : ").strip())

def logic(a, b):
    if (a*b) % 2 == 0:
        return True
    else:
        return False
    
def main():
    a, b = getUserInput()
    result = logic(a, b)
    print(result)
    
if __name__ == "__main__":
    main()