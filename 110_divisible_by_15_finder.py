# 110. Divisible by 15 Finder

# Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.

num_list = [x for x in range(100)]

div_15_list = []
def divisible_by_15(num_list):
    for x in num_list:
        if x%15 == 0:
            div_15_list.append(x)
            
    # print(div_15_list)
            
            

divisible_by_15(num_list)
print(div_15_list)