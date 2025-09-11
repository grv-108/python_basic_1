# 63. Absolute File Path Finder

# Write a Python program to get an absolute file path.

import os

file_name = "63_abs_file_path_finder.py"

print(f"Absolute file path : {os.path.abspath(file_name)}")