# 46. File Path and Name Finder

# Write a Python program to retrieve the path and name of the file currently being executed.

import os

print(f"Current file : {os.path.realpath(__file__)}")