# 32. LCM Calculator

# Write a Python program to find the least common multiple (LCM) of two positive integers.
def getUserInput():
    return int(input("Enter first Number : ").strip()), int(input("Enter second number : ").strip())


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def main():
    a, b = getUserInput()
    result = lcm(a, b)
    print(f"LCM of {a} and {b} will be : {result}")
    
if __name__ == "__main__":
    main()
