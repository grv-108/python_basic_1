# 67. Pressure Unit Converter

# Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.

def getUserInput():
    return float(input("Enter pressure in pascal(Pa) --> ").strip())

def main():
    p = getUserInput()
    ask_user = input("Enter Units.\nPound per square inch(P), Millimeter of Mercury(M), Atmosphere Pressure(A) --> ").strip()
    temp = p
    if ask_user in ['P','p']:
        temp = p/6895
        print(f"Pressure in Pound per square inch(P) : {temp}")
    elif ask_user in ['M','m']:
        temp = p/133.3
        print(f"Pressure in Millimeter of Murcury(M) : {temp}")
    elif ask_user in ['A','a']:
        temp = p/101300
        print(f"Pressure in Atmosphere Pressure(A) : {temp}")
    else:
        print("Enter a valid Unit.")
        
if __name__ == "__main__":
    main()
        
        