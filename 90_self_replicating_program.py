# 90. Self-replicating Program

# Write a Python program to create a copy of its own source code.

with open('rough.py') as f, open('copyFileOfRough.py', 'w') as cp:
    cp.write(f.read())

with open('copyFileOfRough.py') as f:
    for line in f:
        print(line, end = "")
    