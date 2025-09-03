# 23. String Prefix Copies

# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.

def getUserInput():
    return input("Enter string : ").strip(), int(input("How many times you want copy of this string : ").strip())

def main():
    user_str, num_copies = getUserInput()
    
    if len(user_str) < 2:
        print(' '.join([user_str] * num_copies))
    else:
        user_str = user_str[:2]
        print(' '.join([user_str] * num_copies))
        
if __name__ == "__main__":
    main()