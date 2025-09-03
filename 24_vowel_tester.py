# 24. Vowel Tester

# Write a Python program to test whether a passed letter is a vowel or not.

def getUserInput():
    return input("Enter a letter from alphabet : ").strip()

def main():
    user_input = getUserInput()
    if user_input in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        print("Vowel")
    else:
        print("Not vowel")
        
if __name__ == "__main__":
    main()