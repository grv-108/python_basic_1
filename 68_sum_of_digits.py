# 68. Sum of Digits

# Write a Python program to calculate sum of digits of a number.

def getUserInput():
    return int(input("Enter a digit --> ").strip())

def sumOfDigit(number):
    number = abs(number)
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //=10
    return total
    
def main():
    try:
        number = getUserInput()
        result = sumOfDigit(number)
        print(f"Sum of {number} : {result}")
    except ValueError:
        print(f"Invalid number!!!")
    
if __name__ == "__main__":
    main()