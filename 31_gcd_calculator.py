# 31. GCD Calculator

# Write a Python program that computes the greatest common divisor (GCD) of two positive integers.

# def gcg(n1, n2):
    
# n = 12
# n2 =18
# divsible_num1 = []
# for x in range(1, n):
    # if n % x == 0:
        # divsible_num1.append(x)
# divsible_num1 = set(divsible_num1)

# divsible_num2 = []
# for x in range(1, n2):
    # if n2 % x == 0:
        # divsible_num2.append(x)
# divsible_num2 = set(divsible_num2)

# print(divsible_num1)
# print(divsible_num2)



# common_digits = divsible_num2.intersection(divsible_num1)
# print(common_digits)
# gcd = 1

# for x in list(common_digits):
    # gcd *= x
    
# print(gcd)

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

result = gcd(4, 9)
print(result)