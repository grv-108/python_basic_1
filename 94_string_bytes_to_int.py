# 94. String Bytes to Integers

# Write a Python program to convert the bytes in a given string to a list of integers.
import sys
my_str = "It's a python Programming."

str_size = sys.getsizeof(my_str)

int_list = [int(x) for x in str(str_size)]

print(int_list)