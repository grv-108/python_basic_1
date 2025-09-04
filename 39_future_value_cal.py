# 39. Future Value Calculator

# Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

def getUserInput():
    return int(input("Enter amount : ").strip()), float(input("Enter interest rate : ").strip()), int(input("Enter years : ").strip())

def main():
    amt, int_rate, t = getUserInput()
    p = amt*((1+(0.01*int_rate))**t)
    print(f"Future Value : {round(p,2)}")
    
if __name__ == "__main__":
    main()