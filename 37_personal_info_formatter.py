# 37. Personal Info Formatter

# Write a Python program that displays your name, age, and address on three different lines.

def getUserInput():
    return input("Enter your name : ").strip(), int(input("Enter you age : ").strip()), input("Enter your address : ").strip()

def aboutMe(name,age,address):
    print(f"\nMy name is {name.capitalize()}.")
    print(f"I'm {age} years old.")
    print(f"My current location is {address.capitalize()}.\n")
    
def main():
    name, age, address = getUserInput()
    return aboutMe(name,age,address)
    
if __name__ == "__main__":
    main()