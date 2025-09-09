# 58. Sum of First n Positives

# Write a Python program to sum the first n positive integers

def getUserInput():
    return int(input("Enter an integer : ").strip())

def main():
    n = getUserInput()
    # (n*(n+1))/2
    sum = 0
    for i in range(1,n+1):
        sum += i
    print(f"Total sum : {sum}")
    
if __name__ == "__main__":
    main()