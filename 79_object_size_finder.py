# 79. Object Size Finder

# Write a Python program to get the size of an object in bytes.

# to get the size of any object/variable, we can user getsizeof() method of sys module

import sys

name = 'gaurav'
age = 21
height = 5.8
print(f"Size of 'name' var --> {sys.getsizeof(name)} bytes")
print(f"Size of 'age' var --> {sys.getsizeof(age)} bytes")
print(f"Size of 'height' var --> {sys.getsizeof(height)} bytes")

# we can also get the size of other python's data structure like list, tuple, dict etc.

students = ['ram', 'shyam', 'lakhaman', 'sita']
print(f"Size of 'student' list --> {sys.getsizeof(students)} bytes.")