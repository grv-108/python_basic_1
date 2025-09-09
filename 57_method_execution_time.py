# 57. Method Execution Time

# Write a Python program to get the execution time of a Python method.
import time

def getUserInput():
    return int(input("Enter first value : ").strip()), int(input("Enter last value : ").strip())

def main():
    a, b = getUserInput()
    s_time = time.time()
    for i in range(a, b+1):
        print(i, end=", ")
    
    e_time = time.time()
    
    total_time = e_time - s_time
    print(f"\nTotal time take : {total_time}")
    
if __name__ == "__main__":
    main()
    