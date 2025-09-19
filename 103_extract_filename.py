# 103. Extract Filename

# Write a Python program to extract the filename from a given path.
import os

filepath = os.path.abspath("103_extract_filename.py")

filename = [x for x in filepath.split("\\") if x.endswith(".py")]

print(filename[0])


# another solution :-

print(os.path.basename(filepath))