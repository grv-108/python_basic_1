# 65. Seconds to DHMS Converter

# Write a Python program that converts seconds into days, hours, minutes, and seconds.

def getUserInput():
    return int(input("Enter Seconds --> ").strip())

def main():
    user_input = getUserInput()
    ask_user = input("Convert Seconds into days/hours/minutes (D,H,M) --> ").strip()
    temp = 0
    if ask_user in ['D', 'd']:
        temp = user_input//86400
        print(f"{user_input} : {temp} Days")
    elif ask_user in ['H','h']:
        temp = user_input//3600
        print(f"{user_input} : {temp} Hours")
    elif ask_user in ['M','m']:
        temp = user_input//60
        print(f"{user_input} : {temp} Minutes")
    else:
        print("Please enter a valid unit!!!")
    
    
    
if __name__ == "__main__":
    main()