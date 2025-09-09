# 60. Triangle Hypotenuse Calculator

# Write a Python program to calculate the hypotenuse of a right angled triangle.
import math

def getUserInput():
    return float(input("Enter triangle height : ").strip()), float(input("Enter triangle base : ").strip())

def main():
    h, b = getUserInput()
    hyp = round(math.sqrt((h**2) + (b**2)), 2)
    print(f"Hypotenuse of Triangle with Height {h}, and Base {b} : {hyp}")
    
if __name__ == "__main__":
    main()