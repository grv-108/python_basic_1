# 146. Locate Python Module Sources

# Write a Python program to find the location of Python module sources.

import importlib.util as imp

print(imp.find_spec('os'))

print(imp.find_spec('datetime'))