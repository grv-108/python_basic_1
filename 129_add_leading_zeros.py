# 129. Add Leading Zeroes

# Write a Python program to add leading zeroes to a string.

my_num = '3.14'

my_num = my_num.ljust(6,'0')
print(my_num)
my_num = my_num.ljust(8,'0')
print(my_num)

my_num = '3.14'
my_num = my_num.rjust(6,'0')
print(my_num)
my_num = my_num.rjust(8,'0')
print(my_num)