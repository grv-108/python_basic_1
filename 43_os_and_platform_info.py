# 43. OS and Platform Info

# Write a Python program to get OS name, platform and release information.

import platform
import os

def getPlatformInfo():
    print(f"\nOperating System : {os.name.upper()}")
    print(f"\nName of OS System : {platform.system()}")
    print(f"\nVersion of Operating System : {platform.release()}")
    
getPlatformInfo()