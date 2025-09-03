# 21. Even or Odd Checker

# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

def getUserInput():
    return int(input("Enter a number : ").strip())

def even_odd(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 1
    
def main():
    try:
        user_input = getUserInput()
        result = even_odd(user_input)
        if result == 1:
            print("Even")
        elif result == 0:
            print("Zero")
        else:
            print("Odd")
    except ValueError as ve:
        print(f"Invalid input!!!\n{ve}\nPlease enter integer value.")
        
if __name__ == "__main__":
    main()