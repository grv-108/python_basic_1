# 115. List Product Calculator

# Write a Python program to compute the product of a list of integers (without using a for loop).
from functools import reduce

my_list = [x for x in range(1, 11)]
print(f"Original List : {my_list}", end=", ")

prod_list = reduce((lambda x, y: x*y), my_list)
print(f"\nProduct of Original list number : {prod_list}")