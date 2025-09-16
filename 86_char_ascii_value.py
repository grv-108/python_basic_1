# 86. Character ASCII Value

# Write a Python program to get the ASCII value of a character.

def getUserInput():
    return input("Enter a character --> ").strip()

def ascii_value(char):
    if len(char) == 1:
        return f"{char} : {ord(char)}"
    else:
        return "Enter 1 character only!"

def main():
    char = getUserInput()
    result = ascii_value(char)
    print(result)
    
if __name__ == "__main__":
    main()
        