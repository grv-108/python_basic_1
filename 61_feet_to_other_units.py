# 61. Feet to Other Units

# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

def getUserInput():
    return float(input("Enter distance in Feet --> ").strip())

def main():
    try:
        user_input = getUserInput()
        temp = 0
        ask_user = input("Please enter Convert unit\nInches, Yards, Miles (I,Y,M) --> ").strip()
        
        if ask_user in ['I', 'i']:
            temp = user_input * 12
            print(f"\nDistance From Feet to Inches : {temp}")
        elif ask_user in ['Y', 'y']:
            temp = user_input * 0.333333
            print(f"\nDistance from Feet to Yard : {temp}")
        elif ask_user in ['M', 'm']:
            temp = user_input * 0.000189394
            print(f"\nDistance from Feet to Miles : {temp}")
        else:
            print("Please enter Valid Unit.")
    except ValueError():
        print("Invalid Input. Please enter an integer/float value!!!")
        
if __name__ == "__main__":
    main()