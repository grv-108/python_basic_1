# 84. Character Frequency Counter

# Write a Python program to count the number of occurrences of a specific character in a string.

my_str = "hi, my name is gaurav."

char = 'a'

count = 0

for i in my_str:
    if i == char:
        count += 1

print()
print(f"'{char}' appears {count} times in your string.")
print()

# i also have string method count() to count a specific word in a string.

print(my_str.count("a"))