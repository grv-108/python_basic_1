# 66. BMI Calculator

# Write a Python program to calculate the body mass index.

def getUserInput():
    return float(input("Enter Your Weight(kg) --> ").strip()), float(input("Enter Your Height(cm) --> ").strip())

def main():
    w, h = getUserInput()
    h_in_meter = h/100
    bmi = w/(h_in_meter * h_in_meter)
    print(f"Your BMI : {bmi:.2f}")
    
if __name__ == "__main__":
    main()