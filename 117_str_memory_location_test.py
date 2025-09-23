# 117. String Memory Location Test

# Write a Python program to prove that two string variables of the same value point to the same memory location.

a = "hi!"
b = "hi!"

print(hex(id(a)))
print(hex(id(b)))