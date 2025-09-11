# 64. File Timestamps

# Write a Python program that retrieves the date and time of file creation and modification.

import os.path, time

print(f"Last modified : %s " % time.ctime(os.path.getmtime("64_file_timestamps.py")))

print(f"Created at : %s " % time.ctime(os.path.getctime("64_file_timestamps.py")))

print("Nice")