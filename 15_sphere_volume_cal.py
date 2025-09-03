# 15. Sphere Volume Calculator

# Write a Python program to get the volume of a sphere with radius six.

def getUserInput():
    return float(input("Enter radious : "))

r = getUserInput()
volume = 4/3 * (3.14 * r * r * r)
print(f"Volume of Sphere : {round(volume, 2)}")