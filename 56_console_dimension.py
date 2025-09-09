# 56. Console Dimensions

# Write a Python program to get the height and width of the console window.

import fcntl
import termios
import struct

def terminal_size():
    th, tw, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

print(f"Number of columns and rows : {terminal_size()}")