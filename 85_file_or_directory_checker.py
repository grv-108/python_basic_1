# 85. File or Directory Checker

# Write a Python program to check whether a file path is a file or a directory.

import os

path = "85_file_or_directory_checker.py"

if os.path.isdir(path):
    print("It's a directory.")
elif os.path.isfile(path):
    print("It's a file.")
else:
    print("It's a another type file of file.")