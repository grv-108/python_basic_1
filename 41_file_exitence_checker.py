# 41. File Existence Checker

# Write a Python program to check whether a file exists.

import os

def getUserInput():
    return input("Enter file name : ").strip()

def main():
    file_name = getUserInput()
    if os.path.isfile(file_name):
        print(f"\nThe file is present : {file_name}.")
    else:
        print("\nFile is not there!!!")

if __name__ == "__main__":
    main()