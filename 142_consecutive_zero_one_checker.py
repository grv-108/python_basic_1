# 142. Consecutive Zero-One Checker

# Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False.
# Original sequence: 01010101
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# True
# Original sequence: 00
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# False
# Original sequence: 000111000111
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# True
# Original sequence: 00011100011
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# False

def test(input_str):
    while '01' in input_str:
        input_str = input_str.replace('01', '')
    return len(input_str) == 0

my_str = "01010101"

result = test(my_str)
print(result)