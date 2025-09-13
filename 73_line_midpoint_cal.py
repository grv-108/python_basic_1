# 73. Line Midpoint Calculator

# Write a Python program to calculate the midpoints of a line.

def getUserInput():
    return input("Enter A Coordinate points --> ").strip(), input("Enter B Coordinate points --> ").strip()

def midpoint(x1, y1, x2, y2):
    x = (x1+x2)/2
    y = (y1+y2)/2
    return x, y

def main():
    a, b = getUserInput()
    # print(a, b)
    x = a.split(",")
    y = b.split(",")
    # print(x,y)
    # print(float(x[0]), float(y[0]), float(x[1]), float(y[1]))
    resultX, resultY = midpoint(float(x[0]), float(x[1]), float(y[0]), float(y[1]))
    print(f"Line Midpoint : {int(resultX),int(resultY)}")
    
if __name__ == "__main__":
    main()
    