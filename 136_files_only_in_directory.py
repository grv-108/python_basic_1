# 136. Files Only in Directory

# Write a Python program to find files and skip directories in a given directory.

import os
current_dir = print(os.path.dirname(os.path.abspath(__file__)))

from pathlib import Path

current_dir = Path.cwd()
# print(current_dir)

# all_files = list(current_dir.glob("*.py"))
python_files = [file.name for file in current_dir.glob("*.py")]

for f in python_files:
    print(f)