# 40. Distance Between Points

# Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).

import math

def getUserInput():
    a = float(input("Enter X1 : ").strip())
    b = float(input("Enter X2 : ").strip())
    c = float(input("Enter Y1 : ").strip())
    d = float(input("Enter Y2 : ").strip())
    return a, b, c, d

def main():
    x1, x2, y1, y2 = getUserInput()
    formula = math.pow(x2-x1, 2) + math.pow(y2-y1, 2)
    result = round(math.sqrt(formula), 2)
    print()
    print(f"Distance b/w two points : {result}")
    
if __name__ == "__main__":
    main()