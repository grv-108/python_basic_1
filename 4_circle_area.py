def areaOfCircle(r):
    """Area of Circle"""
    return round(3.14 * r * r, 2)
        
def getUserInput():
    return input("Enter radious : ").strip()
        
if __name__ == "__main__":
    try:
        user_input = float(getUserInput())
        result = areaOfCircle(user_input)
        print(result)
    except ValueError as ve:
        print(ve)