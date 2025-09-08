# 52. Print to STDERR

# Write a Python program to print to STDERR.

from __future__ import print_function
import sys

def eprint(*args, **kargs):
    print(*args, file=sys.stderr, **kargs)
    
eprint("abc", "efg", "xyz", sep='--')