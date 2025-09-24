# 134. Input Two Integers

# Write a Python program to input two integers on a single line.

def getUserInput():
    return input("Enter number with space : ").strip()

def main():
    a, b = getUserInput().split(" ")
    
    print(a)
    print(b)
    
if __name__ == "__main__":
    main()