# 104. Process Group and User IDs

# Write a Python program to get the effective group id, effective user id, real group id, and a list of supplemental group ids associated with the current process.
# Note: Availability: Unix.

import os

print("Effective group id : ", os.getegid())

# this is windows :(