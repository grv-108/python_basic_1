# 87. File Size Finder

# Write a Python program to get the size of a file.
import os

file_name = '87_file_size_finder.py'
file_size = os.path.getsize(file_name)
print(f"{file_name} size : {file_size} bytes")
