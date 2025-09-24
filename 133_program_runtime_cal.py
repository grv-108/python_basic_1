# 133. Program Runtime Calculator

# Write a Python program to calculate the time runs (difference between start and current time) of a program.

import time

s_time = time.time()

for x in range(1000):
    print(x, end=",")
    
e_time = time.time()

t_time = s_time - e_time

print()
print()
print()
print(f"Total time take : {t_time}")