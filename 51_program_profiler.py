# 51. Program Profiler

# Write a Python program to determine the profiling of Python programs.

import cProfile

def sum(a, b):
    return a + b

a, b = 5, 5
cProfile.run('sum(a, b)')