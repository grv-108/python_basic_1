# 132. List Home Directory

# Write a Python program to list the home directory without an absolute path.

import os

print(os.path.expanduser("~"))