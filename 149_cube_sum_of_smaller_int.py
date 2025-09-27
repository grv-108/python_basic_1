# 149. Cube Sum of Smaller Integers

# Write a Python function that takes a positive integer and returns the sum of the cube of all positive integers smaller than the specified number.

def getUserInput():
    return int(input("Enter a positive number : ").strip())

def logic(a):
    sum = 0
    for x in range(1, a+1):
        sum += x**3
        
    return sum

def main():
    a = getUserInput()
    result = logic(a)
    print(result)
    
if __name__ == "__main__":
    main()
        
        