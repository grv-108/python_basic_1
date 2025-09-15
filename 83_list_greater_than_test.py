# 83. List Greater-Than Test

# Write a Python program to test whether all numbers in a list are greater than a certain number.

my_list = [90, 12, 45, 83, 18, 39, 28, 100]

check = 10
print(all(i > check for i in my_list))



# checking if elements inside list are greater than 50
# print(f"My list : {my_list}")
# print()

# check = 50
# print(f"Check Value : {check}")

# number_of_values = 0
# print()

# for i in my_list:
#     if i > check:
#         number_of_values += 1
#         print(f"Yes --> {i}")

# print()
# print(f"{number_of_values} values are greater than {check}.")
