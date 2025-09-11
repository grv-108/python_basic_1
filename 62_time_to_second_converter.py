# 62. Time to Seconds Converter

# Write a Python program to convert all units of time into seconds.

def getUserInput():
    return input("Enter time seperated by comma (hh,mm,ss) --> ").strip()

def main():
    user_input = getUserInput().split(",")
    h = int(user_input[0])
    m = int(user_input[1])
    s = int(user_input[2])
    
    seconds = ((h*60)*60)+(m*60)+s
    print(f"{h}/{m}/{s} : {seconds}s")
    
if __name__ == "__main__":
    main()