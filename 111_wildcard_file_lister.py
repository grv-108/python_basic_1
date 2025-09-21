# 111. Wildcard File Lister

# Write a Python program to make file lists from the current directory using a wildcard

import glob

file_list = glob.glob("*.*")
# print(file_list)

print(glob.glob("*.py"))