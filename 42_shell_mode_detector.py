# 42. Shell Mode Detector

# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

import struct

print(f"{struct.calcsize("P") * 8}bit")