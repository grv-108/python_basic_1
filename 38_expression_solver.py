# 38. Expression Solver

# Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

def getUserInput():
    return int(input("Enter x : ").strip()), int(input("Enter y : ").strip())

def main():
    x, y = getUserInput()
    formula = (x+y) * (x+y)
    print(f"\n(x+y)^2 : {formula}")
    
if __name__ == "__main__":
    main()