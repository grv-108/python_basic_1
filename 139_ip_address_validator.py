# 139. IP Address Validator

# Write a Python program to validate an IP address.

import socket

addr = '127.0.0.2561'

try:
    socket.inet_aton(addr)
    print("valid ip.")
except socket.error:
    print("Invalid ip.")