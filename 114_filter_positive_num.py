# 114. Filter Positive Numbers

# Write a Python program to filter positive numbers from a list.

my_list = [1, 2, 3, 4, 5, -2, 0, -2, -1, -89, 2, 0]

pos_num = []
for x in my_list:
    if x > 0:
        pos_num.append(x)

print(pos_num)