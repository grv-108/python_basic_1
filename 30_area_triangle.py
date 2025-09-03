# 30. Triangle Area Calculator

# Write a Python program that will accept the base and height of a triangle and compute its area.

def getUserInput():
    return float(input("Enter base of triangle : ").strip()), float(input("Enter height of triangle : ").strip())

base, height = getUserInput()

area_of_tri = round((1/2)*base*height, 2)
print(area_of_tri)