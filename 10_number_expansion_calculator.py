# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

def logic(n):
    n1 = "%s"% n
    n2 = "%s%s"% (n, n)
    n3 = "%s%s%s"% (n, n, n)
    
    return int(n1),int(n2),int(n3)

n1, n2, n3 = logic(5)
print(n1+n2+n3)

# num = 5
# result = logic(num)
# print(result)