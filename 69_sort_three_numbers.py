# 69. Sort Three Numbers

# Write a Python program to sort three integers without using conditional statements and loops.

def getUserInput():
    return int(input("Enter first number --> ").strip()), int(input("Enter second number --> ").strip()), int(input("Enter third number --> ").strip())

def main():
    a, b, c = getUserInput()
    num_min = min(a, b, c)
    num_max = max(a, b, c)
    num_middle = (a+b+c) - num_min - num_max
    
    print(f"Three Numbers in Order : {num_min, num_middle, num_max}")
    
if __name__ == "__main__":
    main()