# 59. Height to Centimeters

# Write a Python program to convert height (in feet and inches) to centimeters.

def getUserInput():
    return float(input("Enter height : ").strip())

def main():
    height = getUserInput()
    ask = input("If height is in Feet/Inches (F/I) : ").strip()
    
    if ask in ['F','f']:
        print(f"Height Feet to Centimeter : {height*30}")
    elif ask in ['I','i']:
        print(f"Height Inches to Centimeter : {height*2.54}")
    else:
        print("Please enter a valid value!!!")
        
if __name__ == "__main__":
    main()